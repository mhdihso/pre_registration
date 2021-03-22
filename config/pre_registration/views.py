from django.http import request
from rest_framework import permissions, response, status, views, authentication, generics
from django.shortcuts import render
from . import serialaizers
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import main, Create_preـregistration , extra_qu , multiple_options
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class pre_registrationsCreate(ListCreateAPIView):
    queryset= Create_preـregistration.objects.all()
    serializer_class = serialaizers.Createpre_registrationserialaizer
    permission_classes = [IsAdminUser]

class pre_registrationsDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset=Create_preـregistration.objects.all()
    serializer_class=serialaizers.Createpre_registrationserialaizer
    permission_classes=[IsAdminUser]

class pre_registrationformCreate(ListCreateAPIView):
    queryset=main.objects.all()
    serializer_class=serialaizers.pre_registrationserialaizer
    permission_classes=[IsAdminUser]

class pre_registrationformDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset=main.objects.all()
    serializer_class=serialaizers.pre_registrationserialaizer
    permission_classes=[IsAdminUser]

class ExtrafieldDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset= extra_qu.objects.all()
    serializer_class= serialaizers.ExtrafieldSerialaizer 
    permission_classes= [IsAdminUser]

class ExtrafieldCreate(ListCreateAPIView):
    queryset=extra_qu.objects.all()
    serializer_class=serialaizers.ExtrafieldSerialaizer 
    permission_classes=[IsAdminUser]

class AddptionsCreate(ListCreateAPIView):
    queryset=multiple_options.objects.all()
    serializer_class=serialaizers.Addptionsserialaizer
    permission_classes=[IsAdminUser]

class AddptionsDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset=multiple_options.objects.all()
    serializer_class=serialaizers.Addptionsserialaizer
    permission_classes=[IsAdminUser]