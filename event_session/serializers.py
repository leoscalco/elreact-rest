from rest_framework import serializers
from .models import *
from address_session.serializers import AddressSerializer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

class EventSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True)
    tags = TagSerializer(many=True)
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'date',
            'address', 'owner', 'tags')