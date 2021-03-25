from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . import models 

class pre_registrationserialaizer(serializers.ModelSerializer):
    class Meta:
        model=models.PreRegistration
        fields='__all__'

class Createpre_registrationserialaizer(serializers.ModelSerializer):
    class Meta:
        model = models.MainForm
        read_only_fields = ['extra_qus', ]
        fields= '__all__'

class ExtrafieldSerialaizer(serializers.ModelSerializer):
    class Meta:
        model=models.ExtraQu
        fields= '__all__'

class MultipleSerialaizer(serializers.ModelSerializer):
    class Meta:
        model=models.MultipleOptionsData
        fields=['option']

class Addoptionsserialaizer(serializers.ModelSerializer):
    options = MultipleSerialaizer(many=True)
    class Meta:
        model = models.MultipleOptions
        fields = ['Question','options']

    def create(self, validated_data):
        options_data = validated_data.pop('options')
        multiple_add = models.MultipleOptions.objects.create(**validated_data)
        for options_data in options_data:
            models.MultipleOptionsData.objects.create(multiple_add=multiple_add, **options_data)
        return multiple_add

class Answerserialaizer(serializers.ModelSerializer):

    class Meta:
        model = models.ExtraAnsData
        fields=['answer_text','qus']

class Answer_dataserialaizer(serializers.ModelSerializer):

    answers=Answerserialaizer(many=True)

    class Meta:
        model = models.ExtraAns
        fields=['form_id','answers']
    
    def create(self, validated_data):
        answer = validated_data.pop('answers')
        extra_answers = models.ExtraAns.objects.create(**validated_data)
        for answer in answer:
            models.ExtraAnsData.objects.create(extra_answers=extra_answers, **answer)
        return extra_answers