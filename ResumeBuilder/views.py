from django.shortcuts import render, get_object_or_404
from .models import Skill, CourseSkill, UserCourse
from django.http import HttpResponse
from .models import WorkHistory
from .models import Education
from .models import UserInformation




def resume_builder(request):
    users = UserInformation.objects.all()
    return render(request, 'ResumeBuilder/resume_builder.html', {'users': users})

def generated_resume(request):
    if request.method == 'POST':
        user_id = request.POST['user']

    user = get_object_or_404(UserInformation, pk=user_id)

   
    work_experience = WorkHistory.objects.filter(user=user)
    eduction = Education.objects.filter(user=user)
    user_courses = UserCourse.objects.filter(user=user)
        
    user_skills = []

    for user_course in user_courses:
        course_skills = CourseSkill.objects.filter(course_number=user_course.course)
        for course_skill in course_skills:
            user_skills.append(course_skill.skills_id.skill_keyword)


    return render(request, 'ResumeBuilder/generated_resume.html', {'user': user,'work_experience': work_experience, 'education': eduction, 'user_skills': user_skills})

def send_work_history(request):
    users = UserInformation.objects.all()
    if request.method == 'POST':
        company_name = request.POST['cname']
        work_address = request.POST['cadd']
        city = request.POST['ccity']
        state = request.POST['cstate']
        zip = request.POST['czip']
        phone = request.POST['cphone']
        start_date = request.POST['cstart']
        end_date = request.POST['cend']
        # c user
        user_id = request.POST['cuser']
        
        user = get_object_or_404(UserInformation, pk=user_id)

        
        # Conditionals Here for error handling
        
        work_history_entry = WorkHistory.objects.get_or_create(
        company_name = company_name,
        defaults={'user': user, 'work_address': work_address, 'city': city, 'state': state, 'zip': zip, 'phone': phone, 'start_date': start_date, 'end_date': end_date}
        )
    return render(request, 'ResumeBuilder/resume_builder.html', {'users': users})

def send_education(request):
    users = UserInformation.objects.all()
    if request.method == 'POST':
        school_name =request.POST['sname']
        school_state = request.POST['sstate']
        school_city = request.POST['scity']
        degree = request.POST['degree']
        school_start_date =request.POST['sstart']
        school_end_date = request.POST['schoolend']
        # s user
        user_id = request.POST['suser']

        user = get_object_or_404(UserInformation, pk=user_id)

    
        eduction_entry = Education.objects.get_or_create(
            school_name = school_name,
            degree = degree,
            defaults={'user': user,'school_state': school_state,'school_city': school_city,'school_start_date': school_start_date, 'school_end_date': school_end_date}
            )
    return render(request, 'ResumeBuilder/resume_builder.html', {'users': users})



def resume(request):
    keywords = Skill.objects.all()
    return render(request, 'ResumeBuilder/resume_builder.html', {'keywords': keywords})
