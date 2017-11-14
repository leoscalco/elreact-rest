# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins

from rest_framework import viewsets
from event_session.serializers import *
from event_session.models import *
from user_session.models import AppUser, PathInstance
from django.shortcuts import render
from django.contrib.gis.db.models.functions import Distance
from django.db.models import F
from itertools import chain
from django.contrib.gis.geos import Point


# Create your views here.

class EventList(APIView):
    """
    List all addresses, or create a new address
    """
    def get(self, request, format=None):
        # GET RESIDENTIAL
        if (request.GET.get('residential') == 'true'):
            distance_m = 2000
            ref_location = AppUser.objects.get(user=request.user).residentialAddress.point

            ann = Event.objects.annotate(
                distance=Distance('address__point', ref_location))
            # print the distance for each point
            # for a in ann:
            #     print a.name, a.distance

            events = ann.filter(distance__lte=distance_m).order_by('distance', 'date')

        elif (request.GET.get('path') == 'true'):
            distance_m = 500
            # ref_location = AppUser.objects.get(user=request.user).path
            all_points_in_path = PathInstance.objects.filter(
                appUser=AppUser.objects.get(user=request.user)
                )
            events = []
            for a in all_points_in_path:
                print a.address.point
                ann = Event.objects.annotate(
                    distance=Distance('address__point', a.address.point))

                events.append(ann.filter(distance__lte=distance_m).order_by('distance', 'date'))
            # pensar em lista DEPOIS
            events = set(chain.from_iterable(events))

        elif (request.GET.get('current') == 'true'):
            distance_m = 100
            # POINT (LAT, LONG)
            # print type(request.GET.get('lat')), request.GET.get('long')
            ref_location = Point(
                float(request.GET.get('lat')),
                float(request.GET.get('long')),
                srid=4326
                )

            ann = Event.objects.annotate(
                distance=Distance('address__point', ref_location))

            events = ann.filter(distance__lte=distance_m).order_by('distance', 'date')[:1]

        elif (request.GET.get('tags') == 'true'):
            tags = map(lambda x:x.lower(), request.GET.getlist('tag'))
            events = Event.objects.filter(tags__name__in=tags).order_by('date')

        else:
            events = Event.objects.all().order_by('date')

        serializer = EventSerializer(events, many=True)
        # serializer = ObserverVerboseSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(APIView):
    """
    Retrieve, update or delete a address instance.
    """
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        events = self.get_object(pk)
        serializer = EventSerializer(events)
        # serializer = ObserverReadSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        events = self.get_object(pk)
        serializer = EventSerializer(events, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        events = self.get_object(pk)
        events.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
