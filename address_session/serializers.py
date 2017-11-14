from rest_framework import serializers
from .models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        geo_field = 'point'
        fields = ('id', 'zipcode', 'street', 'number',
            'neighbor', 'state', 'country', 'point')