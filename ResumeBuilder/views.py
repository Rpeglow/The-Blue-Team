from django.shortcuts import render
from .models import Skill
from django.http import HttpResponse

def resume(request):
    keywords = Skill.objects.all()
    return render(request, 'ResumeBuilder/resume_builder.html', {'keywords': keywords})
