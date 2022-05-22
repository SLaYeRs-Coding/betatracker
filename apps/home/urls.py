# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('index/', views.index, name='home'),
    path('', views.landing, name='landing'),
    
    path('profile/edit/',views.profileedit,name="edit_profile"),
    path('profile/view/',views.profile,name="view_profile"),
    path('your/valuable/feedback/', views.feedback, name='feedback'),
    path('add/software/',views.add_software,name="add_software"),
    path('all/software/',views.view_all_software,name="all_software"),
    path('all/users/',views.view_all_users,name="all_users"),
    path('download/<int:id>/',views.download,name="download"),
    # Matches any html file
    
]
