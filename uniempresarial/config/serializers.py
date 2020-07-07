# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from .models import *
from common.serializers import *


class UserSerializer(BaseSerializer, serializers.ModelSerializer):
    configs = UserConfigSerializer()

    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'first_name', 'last_name',
                  'email', 'is_active', 'groups', 'configs']


class FacultySerializer(BaseSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class ProgramSerializer(BaseSerializer):
    class Meta:
        model = Program
        fields = '__all__'


class ScheduleModelSerializer(BaseSerializer):
    class Meta:
        model = ScheduleModel
        fields = '__all__'


class PromotionModelSerializer(BaseSerializer):
    class Meta:
        model = PromotionModel
        fields = '__all__'


class AccountModelSerializer(BaseSerializer):
    auth_user = UserNestedSerializer(read_only=True)
    auth_user_id = serializers.IntegerField(write_only=True)
    faculty = FacultySerializer(read_only=True)
    faculty_id = serializers.IntegerField(write_only=True)
    program = ProgramSerializer(read_only=True)
    program_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = AccountModel
        fields = '__all__'


class ModuleConfigSerializer(BaseSerializer):
    class Meta:
        model = ModuleConfig
        fields = '__all__'


class RolConfigSerializer(BaseSerializer):
    modules = ModuleConfigSerializer(many=True, read_only=True)

    class Meta:
        model = ModuleConfig
        fields = ('id', 'external_id', 'name', 'description', 'status')


class RolUserSerializer(BaseSerializer):
    account = AccountModelSerializer(read_only=True)
    account_id = serializers.IntegerField(write_only=True)
    config = RolConfigSerializer(read_only=True)
    config_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = RolUser
        fields = '__all__'
