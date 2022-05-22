# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    '''Admin View for Application'''

    list_display = ('user','developer_post','category','app_name','stage','description','logo','company','version','size','setup','created_on','updated_on','is_approved',)
    search_fields = ('user',)
   
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('name','logo',)
    search_fields = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Profile'''

    list_display = ('user','image','bio','gender','github_link','linkedin_link',)
    search_fields = ('user',)
  
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    '''Admin View for Feedback'''

    list_display = ('name','email','contact_no','description',)
    search_fields = ('name',)
  