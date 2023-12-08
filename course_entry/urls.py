from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
from .views import image_page, image_detail, about, FAQ, success_page, user_logout

urlpatterns = [
    
    path('', image_page, name='image_page'),
    path('course_list/', views.course_list, name='course_list'),
    path('image/<int:image_id>', image_detail, name='image_detail'),
    path('about/', about, name='about'),
    path('FAQ/', FAQ, name='FAQ'),
    path('login/', auth_views.LoginView.as_view(template_name='course_entry/login.html'), name='login'),
    path('logout/', user_logout, name='logout'),
    path('success/', success_page, name='success_page')
]