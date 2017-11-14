from rest_framework import serializers
from .models import *
from address_session.models import *
from address_session.serializers import AddressSerializer
from django.contrib.auth import get_user_model

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ('id', 'type')

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
            'last_name', 'email',
            'last_login', 'date_joined', 'is_staff',
            'password'
            )

class EventOwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = EventOwner
        fields = ('id', 'user',
            'occupation', 'userType', 'phone'
            )

    def create(self, validated_data):
        UserModel = get_user_model()
        user_pop = validated_data.pop("user")

        print user_pop

        new_user = UserModel.objects.create(
            username=user_pop['username'],
            first_name=user_pop['first_name'],
            last_name=user_pop['last_name'],
            email=user_pop['email']
            )

        new_user.set_password(user_pop['password'])
        new_user.save()

        eventOwner = EventOwner.objects.create(
            user=new_user,
            occupation=validated_data['occupation'],
            userType=UserType.objects.get(type__exact='EventOwner'),
            phone=validated_data['phone']
            )

        return eventOwner

class AppUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    userType = UserTypeSerializer()
    residentialAddress = AddressSerializer()
    # path = PathSerializer(source="path_set", many=True)
    class Meta:
        model = AppUser
        fields = ('id', 'user', 'userType',
            'phone', 'residentialAddress'
            )

class PathSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    # appUser = AppUserSerializer()
    # address_ = serializers.ReadOnlyField(source="address.point")
    # print address_
    class Meta:
        model = PathInstance
        fields = ('id', 'date', 'address')