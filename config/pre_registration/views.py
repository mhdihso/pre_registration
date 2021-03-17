from django.http import request
from rest_framework import permissions, response, status, views, authentication, generics
from django.shortcuts import render
from . import serialaizers
from rest_framework.generics import ListCreateAPIView , RetrieveAPIView
from .models import main, Create_preـregistration , preـregistration
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class pre_registrationList(ListCreateAPIView):
    queryset= preـregistration.objects.all()
    serializer_class = serialaizers.pre_registrationserialaizer
    permission_classes = [IsAdminUser]

class pre_registrationDetail(RetrieveAPIView):
    queryset=preـregistration.objects.all()
    serializer_class=serialaizers.pre_registrationserialaizer
    permission_classes=[IsAdminUser]

class pre_registrationCreate(ListCreateAPIView):
    queryset=Create_preـregistration.objects.all()
    serializer_class=serialaizers.Createpre_registrationserialaizer
    permission_classes=[IsAdminUser]