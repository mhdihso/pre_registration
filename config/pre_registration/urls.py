from django.urls import path
from . import views

app_name='pre_registration'

urlpatterns = [
    path('', views.pre_registrationList.as_view()),
    path('<int:pk>', views.pre_registrationDetail.as_view()),
    path('create',views.pre_registrationCreate.as_view())
]