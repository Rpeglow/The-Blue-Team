from django.urls import path 
from . import views
from .views import image_page, image_detail, about, FAQ

urlpatterns = [
    
    path('', image_page, name='image_page'),
    path('course_list/', views.course_list, name='course_list'),
    path('image/<int:image_id>', image_detail, name='image_detail'),
    path('about/', views.about, name='about'),
    path('FAQ/', views.FAQ, name='FAQ')
]