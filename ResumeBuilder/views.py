from django.shortcuts import render
from .models import Skill
from django.http import HttpResponse
from .models import WorkHistory
from .models import Education

def send_work_history(request):
    if request.method == 'POST':
        company_name = request.POST['cname']
        work_address = request.POST['cadd']
        city = request.POST['ccity']
        state = request.POST['cstate']
        zip = request.POST['czip']
        phone = request.POST['cphone']
        start_date = request.POST['cstart']
        end_date = request.POST['cend']
        # user info
        
        # Conditionals Here for error handling
        
        work_history_entry = WorkHistory(company_name, work_address, city, state, zip, phone, start_date, end_date)
        work_history_entry.save()
    return render(request, 'ResumeBuilder/resumer_builder.html', {})

def send_edcation(request):
    if request.method == 'POST':
        school_name =request.POST['sname']
        school_state = request.POST['sstate']
        school_city = request.POST['scity']
        degree = request.POST['degree']
        school_start_date =request.POST['sstart']
        school_end_date = request.POST['schoolend']
    
        eduction_entry = Education(school_name,school_state,school_city,degree,school_start_date, school_end_date)
        eduction_entry.save()
    return render(request, 'ResumeBuilder/resumer_builder.html', {})

def resume(request):
    keywords = Skill.objects.all()
    return render(request, 'ResumeBuilder/resume_builder.html', {'keywords': keywords})
