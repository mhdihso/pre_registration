from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import main ,Create_preـregistration , main , extra_qu , multiple_options

class pre_registrationserialaizer(serializers.ModelSerializer):
    class Meta:
        model = main
        read_only_fields = ['extra_qus', ]
        fields= '__all__'

class Createpre_registrationserialaizer(serializers.ModelSerializer):
    class Meta:
        model=Create_preـregistration
        fields='__all__'

class ExtrafieldSerialaizer(serializers.ModelSerializer):
    class Meta:
        model=extra_qu
        fields= '__all__'

class Addptionsserialaizer(serializers.ModelSerializer):
    class Meta:
        model = multiple_options
        fields = '__all__'