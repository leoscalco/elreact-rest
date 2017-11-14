# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from address_session.models import Address
from user_session.models import EventOwner
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.name

class Event(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=600)
    date = models.DateTimeField()
    address = models.ManyToManyField(Address)
    owner = models.ForeignKey(EventOwner)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return u'%s' % self.name