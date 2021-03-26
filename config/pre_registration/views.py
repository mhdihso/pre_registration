from django.http import request
from rest_framework import permissions, response, status, views, authentication, generics
from django.shortcuts import render
from . import serialaizers
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView , ListAPIView,CreateAPIView
from . import models 
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.settings import api_settings
from rest_framework.response import Response

class pre_registrationsCreate(ListCreateAPIView):

    # def get_queryset(self):
    #     return models.PreRegistration.objects.filter(school_id=self.request.user.school_id).select_related('user')

    queryset= models.PreRegistration.objects.all()
    serializer_class = serialaizers.pre_registrationserialaizer
    permission_classes = [IsAdminUser]

class pre_registrationsDetail(RetrieveUpdateDestroyAPIView):

    # def get_queryset(self):
    #     return models.PreRegistration.objects.filter(school_id=self.request.user.school_id).select_related('user')

    lookup_field = 'id'
    queryset= models.PreRegistration.objects.all()
    serializer_class=serialaizers.pre_registrationserialaizer
    permission_classes=[IsAdminUser]

class pre_registrationformCreate(CreateAPIView):

    serializer_class=serialaizers.Createpre_registrationserialaizer
    permission_classes=[IsAdminUser]

class pre_registrationformList(ListAPIView):

    # def get_queryset(self , *args, **kwargs):
    #     return models.MainForm.objects.filter(pre_id.shool_id=self.request.user.school_id),pre_id=self.kwargs['id'])

    def get_queryset(self , *args, **kwargs):
        return models.MainForm.objects.filter(pre_id=self.kwargs['id'])

    serializer_class=serialaizers.Createpre_registrationserialaizer
    permission_classes=[IsAdminUser]

class pre_registrationformDetail(RetrieveUpdateDestroyAPIView):

    # def get_queryset(self , *args, **kwargs):
    #     return models.MainForm.objects.filter(pre_id.shool_id=self.request.user.school_id),pre_id=self.kwargs['id'])

    def get_queryset(self , *args, **kwargs):
        return models.MainForm.objects.filter(pre_id=self.kwargs['id'])
    
    lookup_field = 'id'
    serializer_class=serialaizers.Createpre_registrationserialaizer
    permission_classes=[IsAdminUser]

class ExtrafieldDetail(RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return models.ExtraQu.objects.filter(form_id=self.kwargs['id'])

    lookup_field = 'id'
    serializer_class= serialaizers.ExtrafieldSerialaizer 
    permission_classes= [IsAdminUser]
    
class ExtrafieldCreate(CreateAPIView):

    serializer_class=serialaizers.ExtrafieldSerialaizer 
    permission_classes=[IsAdminUser]

class ExtrafieldList(ListAPIView):

    def get_queryset(self):
        return models.ExtraQu.objects.filter(form_id=self.kwargs['id'])

    serializer_class=serialaizers.ExtrafieldSerialaizer 
    permission_classes=[IsAdminUser]


class optionsList(ListAPIView):
    queryset=models.MultipleOptions.objects.all()
    serializer_class=serialaizers.Addoptionsserialaizer
    permission_classes=[IsAdminUser]


class Addoptions(CreateAPIView):
    serializer_class=serialaizers.Addoptionsserialaizer
    permission_classes=[IsAdminUser]

    def create(self, request, *args, **kwargs):
        data=request.data
        qus=data.get('Question')
        valu=models.ExtraQu.objects.get(id=qus)
        typ=valu.type_qu
        typ=str(typ)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if typ == "1":
            self.perform_create(serializer)
        else:
            return Response ({"message":"ERROR,This is not a multiple choice question"},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
         
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class optionDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset=models.MultipleOptions.objects.all()
    serializer_class=serialaizers.Addoptionsserialaizer
    permission_classes=[IsAdminUser]

class ExtraanswerList(ListAPIView):
    queryset=models.ExtraAns.objects.all()
    serializer_class=serialaizers.Answer_dataserialaizer
    permission_classes=[IsAdminUser]

class ExtraanswerCreate(CreateAPIView):
    serializer_class=serialaizers.Answer_dataserialaizer
    permission_classes=[IsAdminUser]

    def create(self, request, *args, **kwargs):
        Correctnessـofـinformation=True
        data=request.data
        x=data.get('answers')
        p=data.get('form_id')
        for i in x:
            y=i.get('qus')
            valu=models.ExtraQu.objects.get(id=y)
            form=valu.form_id
            form=str(form)
            p=str(p)
            if form != p :
                Correctnessـofـinformation = False
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if Correctnessـofـinformation == True :
            self.perform_create(serializer)
        else:
            return Response ({"message":"ERROR,This pre-registration does not have this fields"},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

class ExtraanswerDetail(RetrieveUpdateDestroyAPIView):
    queryset=models.ExtraAns.objects.all()
    serializer_class=serialaizers.Answer_dataserialaizer
    permission_classes=[IsAdminUser]