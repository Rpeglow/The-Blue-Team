from django.urls import path 
from . import views

urlpatterns = [
    path('', views.user_info_form, name='user_info_form')
]
