from django.http import request
from rest_framework import permissions, response, status, views, authentication, generics
from django.shortcuts import render
from . import serialaizers
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from . import models 
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.settings import api_settings
from rest_framework.response import Response

class pre_registrationsCreate(ListCreateAPIView):
    queryset= models.PreRegistration.objects.all()
    serializer_class = serialaizers.pre_registrationserialaizer
    permission_classes = [IsAdminUser]

class pre_registrationsDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset= models.PreRegistration.objects.all()
    serializer_class=serialaizers.pre_registrationserialaizer
    permission_classes=[IsAdminUser]

class pre_registrationformCreate(ListCreateAPIView):
    queryset=models.MainForm.objects.all()
    serializer_class=serialaizers.Createpre_registrationserialaizer
    permission_classes=[IsAdminUser]

class pre_registrationformDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset=models.MainForm.objects.all()
    serializer_class=serialaizers.Createpre_registrationserialaizer
    permission_classes=[IsAdminUser]

class ExtrafieldDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset= models.ExtraQu.objects.all()
    serializer_class= serialaizers.ExtrafieldSerialaizer 
    permission_classes= [IsAdminUser]
    
class ExtrafieldCreate(ListCreateAPIView):
    queryset= models.ExtraQu.objects.all()
    serializer_class=serialaizers.ExtrafieldSerialaizer 
    permission_classes=[IsAdminUser]

class AddoptionsCreate(ListCreateAPIView):
    queryset=models.MultipleOptions.objects.all()
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


class AddoptionsDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset=models.MultipleOptions.objects.all()
    serializer_class=serialaizers.Addoptionsserialaizer
    permission_classes=[IsAdminUser]

class Extraanswer(ListCreateAPIView):
    queryset=models.ExtraAns.objects.all()
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
