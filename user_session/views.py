# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins

from rest_framework import viewsets
from user_session.serializers import *
from user_session.models import *
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.

@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"},
            status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})

class EventOwnerList(APIView):
    permission_classes = (IsAuthenticated,)
    """
    List all event owners, or create a new owner
    """
    def get(self, request, format=None):
        eventowners = EventOwner.objects.all()
        serializer = EventOwnerSerializer(eventowners, many=True)
        # serializer = ObserverVerboseSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventOwnerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventOwnerDetail(APIView):
    permission_classes = (IsAuthenticated,)

    """
    Retrieve, update or delete a address instance.
    """
    def get_object(self, pk):
        try:
            return EventOwner.objects.get(pk=pk)
        except EventOwner.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        eventowners = self.get_object(pk)
        serializer = EventOwnerSerializer(eventowners)
        # serializer = ObserverReadSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        eventowners = self.get_object(pk)
        serializer = EventOwnerSerializer(eventowners, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        eventowners = self.get_object(pk)
        eventowners.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AppUserList(APIView):
    """
    List all event owners, or create a new owner
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        appusers = AppUser.objects.all()
        serializer = AppUserSerializer(appusers, many=True)
        # serializer = ObserverVerboseSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AppUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppUserDetail(APIView):
    """
    Retrieve, update or delete a address instance.
    """
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return AppUser.objects.get(pk=pk)
        except AppUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        appusers = self.get_object(pk)
        serializer = AppUserSerializer(appusers)
        # serializer = ObserverReadSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        appusers = self.get_object(pk)
        serializer = AppUserSerializer(appusers, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        appusers = self.get_object(pk)
        appusers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PathList(APIView):
    """
    List all event owners, or create a new owner
    """
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        if ('appuser' in request.GET):
            paths = PathInstance.objects.filter(appUser_id=request.GET.get('appuser'))
        else:
            paths = PathInstance.objects.all()
        serializer = PathSerializer(paths, many=True)
        # serializer = ObserverVerboseSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PathSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PathDetail(APIView):
    """
    Retrieve, update or delete a address instance.
    """
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return PathInstance.objects.get(pk=pk)
        except PathInstance.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        paths = self.get_object(pk)
        serializer = PathSerializer(paths)
        # serializer = ObserverReadSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        paths = self.get_object(pk)
        serializer = PathSerializer(paths, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        paths = self.get_object(pk)
        paths.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
