# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="category")

    class Meta:
        verbose_name_plural = 'categories'

    def str(self):
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile")
    bio = models.TextField()
    gender = models.CharField(max_length=255)
    github_link = models.URLField()
    linkedin_link = models.URLField()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return self.developer_name


class Application(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    developer_post = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    app_name = models.CharField(max_length=255)
    stage = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    logo = models.ImageField(upload_to="logo")
    company = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    size_type = models.CharField(max_length=225)
    setup = models.FileField(upload_to="setups")
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Application."""

        verbose_name = 'Application'
        verbose_name_plural = 'Applications'

    def __str__(self):
        """Unicode representation of Application."""
        return self.app_name


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_no = models.CharField(max_length=255)
    description = models.TextField()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Feedback."""

        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        """Unicode representation of Feedback."""
        return self.name
