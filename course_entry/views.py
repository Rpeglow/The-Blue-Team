from django.shortcuts import render
from .models import Course

# Create your views here.
def course_list(request):
    return render(request, 'course_entry/course_list.html', {})