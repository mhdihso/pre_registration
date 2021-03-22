from django.urls import path
from . import views

app_name='pre_registration'

urlpatterns = [
    path('', views.pre_registrationsCreate.as_view()),
    path('<int:id>', views.pre_registrationsDetail.as_view()),
    path('fill',views.pre_registrationformCreate.as_view()),
    path('fill/<int:id>',views.pre_registrationformDetail.as_view()),
    path('create/extra_field',views.ExtrafieldCreate.as_view()),
    path('create/extra_field/<int:id>',views.ExtrafieldDetail.as_view()),
    path('create/extra_filed/options',views.AddptionsCreate.as_view()),
    path('create/extra_filed/options/<int:id>',views.AddptionsDetail.as_view()),
]
