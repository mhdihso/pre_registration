from django.urls import path
from . import views

app_name='pre_registration'

urlpatterns = [
    path('', views.pre_registrationsCreate.as_view()),
    path('<int:id>', views.pre_registrationsDetail.as_view()),
    path('form',views.pre_registrationformCreate.as_view()),
    path('forms/<int:id>',views.pre_registrationformList.as_view()),
    path('form/<int:id>',views.pre_registrationformDetail.as_view()),
    path('create/extra_field',views.ExtrafieldCreate.as_view()),
    path('create/extra_fields/<int:id>',views.ExtrafieldList.as_view()),
    path('create/extra_field/<int:id>',views.ExtrafieldDetail.as_view()),
    path('create/extra_field/answer',views.ExtraanswerCreate.as_view()),
    path('create/extra_field/answers',views.ExtraanswerList.as_view()),
    path('create/extra_field/answer',views.ExtraanswerDetail.as_view()),
    path('create/extra_field/addoptions',views.Addoptions.as_view()),
    path('create/extra_field/options',views.optionsList.as_view()),

]
