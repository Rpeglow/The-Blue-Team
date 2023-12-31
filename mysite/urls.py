"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'course_entry.views.error_404_view'
handler500 = 'course_entry.views.error_500_view'

urlpatterns = [
    path('',include('course_entry.urls')),
    path('admin/', admin.site.urls),
    path('newuser/', include('UserInfo.urls')),
    path('classtracker/', include('ClassTracker.urls')),
    path('resumebuilder/', include('ResumeBuilder.urls')),
    path('jobsearch/', include('JobSearch.urls'))
 ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
