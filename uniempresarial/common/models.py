# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='+', null=True,  on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, related_name='+', null=True,  on_delete=models.CASCADE)

    class Meta:
        abstract = True


class ViewModel(object):
    def save(self, *args, **kwargs):
        return

    def delete(self, *args, **kwargs):
        return
