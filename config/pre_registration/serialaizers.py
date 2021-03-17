from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import main ,Create_preـregistration , preـregistration

class pre_registrationserialaizer(serializers.ModelSerializer):
    class Meta:
        model = preـregistration
        read_only_fields = ['extra_qus', ]
        fields= '__all__'

class Createpre_registrationserialaizer(serializers.ModelSerializer):
    class Meta:
        model=Create_preـregistration
        fields='__all__'