from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_tracker, name='class_tracker'),
    path('search/', views.search_course, name='search_course'),
]
