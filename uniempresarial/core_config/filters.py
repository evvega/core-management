# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django_filters
from common.models import *
from .models import *


class FacultyFilter(django_filters.FilterSet):
    class Meta:
        model = Faculty
        fields = ['external_id', 'name']


class ProgramFilter(django_filters.FilterSet):
    class Meta:
        model = Program
        fields = ['external_id', 'name']


class ScheduleModelFilter(django_filters.FilterSet):
    class Meta:
        model = ScheduleModel
        fields = ['external_id', 'name']


class PromotionModelFilter(django_filters.FilterSet):
    class Meta:
        model = PromotionModel
        fields = ['external_id', 'name']


class AccountModelFilter(django_filters.FilterSet):
    class Meta:
        model = AccountModel
        fields = ['code_id', 'auth_user_id', 'faculty_id', 'program_id', 'schedule_id']


class ModuleConfigFilter(django_filters.FilterSet):
    class Meta:
        model = ModuleConfig
        fields = ['external_id', 'name', 'url', 'status_id']


class RolConfigFilter(django_filters.FilterSet):
    module_id = django_filters.CharFilter(field_name="configs__modules")

    class Meta:
        model = RolConfig
        fields = ['external_id', 'name', 'description', 'status_id', 'module_id']


class RolUserFilter(django_filters.FilterSet):

    class Meta:
        model = RolUser
        fields = ['account_id', 'config_id']
