# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Employee,new_model
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','country','city','salary']

@admin.register(new_model)
class CsvAdmin(admin.ModelAdmin):
    # list_display2 = ['user','X','Y','country','city','salary', 'deg1_x0', 'deg1_x1', 'deg1_accuracy', 'deg1_intercept',
    #                 'deg2_x0', 'deg2_x1', 'deg2_x2', 'deg2_accuracy', 'deg2_intercept', 'deg3_x0', 'deg3_x1', 'deg3_x2',
    #                 'deg3_x3', 'deg3_accuracy', 'deg3_intercept', 'deg4_x0', 'deg4_x1', 'deg4_x2', 'deg4_x3', 'deg4_x4',
    #                  'deg4_accuracy', 'deg4_intercept']
    list_display2 = ['id', 'X', 'Y']