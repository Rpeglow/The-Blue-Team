from django.urls import path 
from . import views
from .views import image_page, image_detail, about, FQA

urlpatterns = [
    
    path('', image_page, name='image_page'),
    path('course_list/', views.course_list, name='course_list'),
    path('image/<int:image_id>', image_detail, name='image_detail'),
    path('about/', views.about, name='about'),
    path('FQA/', views.FQA, name='FQA')
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
]
