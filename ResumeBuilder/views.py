from django.shortcuts import render, get_object_or_404
from .models import Skill
from django.http import HttpResponse
from .models import WorkHistory
from .models import Education
from .models import UserInformation


def resume_builder(request):
    users = UserInformation.objects.all()
    return render(request, 'ResumeBuilder/resume_builder.html', {'users': users})

def generated_resume(request):
    work_experience = WorkHistory.objects.all()
    eduction = Education.objects.all()
    user_skills = Skill.objects.all()
    return render(request, 'ResumeBuilder/generated_resume.html', {'work_experience': work_experience, 'education': eduction, 'user_skills': user_skills})

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
        user_id = request.POST['user']
        
        user = get_object_or_404(UserInformation, pk=user_id)

        
        # Conditionals Here for error handling
        
        work_history_entry = WorkHistory.objects.get_or_create(
        company_name = company_name,
        defaults={'user': user, 'work_address': work_address, 'city': city, 'state': state, 'zip': zip, 'phone': phone, 'start_date': start_date, 'end_date': end_date}
        )
    return render(request, 'ResumeBuilder/resume_builder.html', {})

def send_education(request):
    if request.method == 'POST':
        school_name =request.POST['sname']
        school_state = request.POST['sstate']
        school_city = request.POST['scity']
        degree = request.POST['degree']
        school_start_date =request.POST['sstart']
        school_end_date = request.POST['schoolend']
        user_id = request.POST['user']

        user = get_object_or_404(UserInformation, pk=user_id)

    
        eduction_entry = Education.objects.get_or_create(
            school_name = school_name,
            degree = degree,
            defaults={'user': user,'school_state': school_state,'school_city': school_city,'school_start_date': school_start_date, 'school_end_date': school_end_date}
            )
    return render(request, 'ResumeBuilder/resume_builder.html', {})



def resume(request):
    keywords = Skill.objects.all()
    return render(request, 'ResumeBuilder/resume_builder.html', {'keywords': keywords})
