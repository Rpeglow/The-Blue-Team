from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_search, name='job_search'),
    path('fetch_skills/<int:user_id>/', views.fetch_skills, name='fetch_skills'),
    path('search/', views.confirm_job_search, name='confirm_job_search'),
    path('list/', views.load_previous_jobs, name='load_previous_jobs')
    ]
