from django.shortcuts import render, get_object_or_404
from .models import Image

# Create your views here.
def course_list(request):
    return render(request, 'course_entry/course_list.html', {})

def image_page(request):
    images = Image.objects.all()
    return render(request, 'course_entry/image_page.html', {'images': images})

def image_detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    return render(request, 'course_entry/image_detail.html', {'image': image})