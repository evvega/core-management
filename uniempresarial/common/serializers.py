# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from .models import *


class UserNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',
                  'email']


class BaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, allow_null=True)
    created_by = UserNestedSerializer(read_only=True)
    modified_by = UserNestedSerializer(read_only=True)

    def __init__(self, *args, **kwargs):
        super(BaseSerializer, self).__init__(*args, **kwargs)
        self.add_timestamp_fields()

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        validated_data['modified_by'] = self.context['request'].user
        return super(BaseSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data['modified_by'] = self.context['request'].user
        return super(BaseSerializer, self).update(instance, validated_data)

    def add_timestamp_fields(self):
        for field in list(self.fields):
            if type(self.fields[field]) == serializers.DateTimeField or type(self.fields[field]) == serializers.DateField:
                field_name = "{}_timestamp".format(field)
                self.fields[field_name] = TimestampField(source=self.fields[field].source)
