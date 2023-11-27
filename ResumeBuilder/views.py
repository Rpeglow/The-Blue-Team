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

def resume(request):
    keywords = Skill.objects.all()
    return render(request, 'ResumeBuilder/resume_builder.html', {'keywords': keywords})
