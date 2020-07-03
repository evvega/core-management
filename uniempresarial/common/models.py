# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='+', null=True)
    modified_by = models.ForeignKey(User, related_name='+', null=True)

    class Meta:
        abstract = True


class StateModel(BaseModel):
    external_id = models.CharField(max_length=15, unique=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

    class Meta:
        abstract = True


class ViewModel(object):
    def save(self, *args, **kwargs):
        return

    def delete(self, *args, **kwargs):
        return
