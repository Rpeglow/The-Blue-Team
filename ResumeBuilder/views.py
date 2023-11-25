from django.shortcuts import render
from django.http import HttpResponse

def resume(request):
    return render(request, 'resume_builder.html')
