from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_builder, name='resume_builder'),
    path('send_work_history', views.send_work_history, name='send_work_history'),
    path('send_education', views.send_education, name='send_education')
]