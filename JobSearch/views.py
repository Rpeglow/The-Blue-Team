from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Job
from UserInfo.models import UserInformation
from ClassTracker.models import CourseSkill, UserCourse
from .indeed import perform_job_search

def job_search(request):
    """
    Renders the job search page.

    Args:
        request (HttpRequest): The HTTP request.
    
    Returns:
        HttpResponse: The HTTP response.
    """
    users = UserInformation.objects.all()
    return render(request, 'job_search.html', {'users': users})

def fetch_skills(request, user_id):
    """
    Fetches the skills associated with a user.

    Args:
        request (HttpRequest): The HTTP request.
        user_id (int): The id of the user.
    
    Returns:
        JsonResponse: The JSON response.
    """
    user = get_object_or_404(UserInformation, pk=user_id)
    user_courses = UserCourse.objects.filter(user=user)
    
    associated_skills = []

    for user_course in user_courses:
        course_skills = CourseSkill.objects.filter(course_number=user_course.course)
        for course_skill in course_skills:
            associated_skills.append(course_skill.skills_id.skill_keyword)

    return JsonResponse({'skills': associated_skills})

def confirm_job_search(request):
    """
    Renders the job search confirmation page.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The HTTP response.
    """
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        keywords = request.POST.getlist('selected_skills')

        if user_id and keywords:
            user = UserInformation.objects.get(pk=user_id)
            user_location = user.city + ", " + user.state

            jobs = perform_job_search(keywords=keywords, location=user_location)

            if jobs:
                for job_data in jobs:
                    existing_job = Job.objects.filter(job_name=job_data['job_name']).first()
                    if not existing_job:
                        job = Job.objects.create(
                            user=user,
                            job_name=job_data['job_name'],
                            salary_range=job_data['salary_range'],
                            description=job_data['description'],
                            hyperlink=job_data['hyperlink']
                        )
                        job.save()
                        
                return render(request, 'job_list.html', {'jobs': jobs})

    return render(request, 'no_jobs_found.html')


def load_previous_jobs(request):
    """
    Renders the job list page.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The HTTP response.
    """
    if request.method == 'POST':
        user_id = request.POST.get('p_user_id')

        if user_id:
            user = UserInformation.objects.get(pk=user_id)  
    
            jobs = Job.objects.filter(user=user)
            
            return render(request, 'job_list.html', {'jobs': jobs})