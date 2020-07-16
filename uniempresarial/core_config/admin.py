# -*- coding: utf-8 -*-
from django.apps import apps
from django.contrib import admin

# auto-register all models
app = apps.get_app_config('core_config')


for model_name, model in app.models.items():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
