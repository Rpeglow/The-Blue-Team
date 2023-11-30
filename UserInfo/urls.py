from django.urls import path 
from . import views

urlpatterns = [
    path('', views.user_info_form, name='user_info_form'),
    path('confirmation/', views.confirmation_page, name='confirmation_page')
]
