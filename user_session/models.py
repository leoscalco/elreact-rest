# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from address_session.models import Address
from datetime import datetime

# Create your models here.

class UserType(models.Model):
    type = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return u'%s' % self.type

class EventOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=200, blank=True)
    userType = models.ForeignKey(UserType)
    phone = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return u'%s' % self.user.email

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userType = models.ForeignKey(UserType)
    phone = models.CharField(max_length=30, blank=True)
    residentialAddress = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="residential")
    path = models.ManyToManyField(Address, through='PathInstance')

    def __unicode__(self):
        return u'%s' % self.user.email

class PathInstance(models.Model):
    appUser = models.ForeignKey(AppUser)
    address = models.ForeignKey(Address, related_name="address_point")
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s - %s' % (self.appUser.user.email, datetime.strftime(self.date, '%d/%m/%Y %H:%M:%S'))
