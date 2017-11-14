# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=150)
    number = models.IntegerField()
    zipcode = models.CharField(max_length=150)
    neighbor = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    # mpoly = models.MultiPolygonField()
    point = models.PointField(default=Point(1, 1))

    def __str__(self):
        return self.street

    def __unicode__(self):
        return u'%s' % self.street
