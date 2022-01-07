# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
#for csv
from django.contrib.auth.models import User
from django.db.models.base import Model
from numpy import mod

class new_model(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    X=models.CharField(max_length=100)
    Y=models.CharField(max_length=100)
    # date=models.DateField()
    # deg1_x0=models.FloatField()
    # deg1_x1=models.FloatField()
    # deg1_accuracy=models.FloatField()
    # deg1_intercept=models.FloatField()
    # deg2_x0=models.FloatField()
    # deg2_x1=models.FloatField()
    # deg2_x2=models.FloatField()
    # deg2_accuracy=models.FloatField()
    # deg2_intercept=models.FloatField()
    # deg3_x0=models.FloatField()
    # deg3_x1=models.FloatField()
    # deg3_x2=models.FloatField()
    # deg3_x3=models.FloatField()
    # deg3_accuracy=models.FloatField()
    # deg3_intercept=models.FloatField()
    # deg4_x0=models.FloatField()
    # deg4_x1=models.FloatField()
    # deg4_x2=models.FloatField()
    # deg4_x3=models.FloatField()
    # deg4_x4=models.FloatField()
    # deg4_accuracy=models.FloatField()
    # deg4_intercept=models.FloatField()

class Employee(models.Model):
    name = models.CharField(max_length=65)
    country = models.CharField(max_length=65)
    city = models.CharField(max_length=65)
    salary = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

class SyllabusPieModel(models.Model):
    subject_name=models.CharField(max_length=20)
    score=models.PositiveIntegerField()
    colors=models.CharField(max_length=25,default='gray')
    explode=models.PositiveIntegerField()

