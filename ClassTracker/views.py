from django.shortcuts import render, get_object_or_404
from UserInfo.models import UserInformation
from .models import Course, Skill, CourseSkill, UserCourse
from .scraping import scrape_course_data
from .ai import generate_skills_from_description

def class_tracker(request):
    """
    Renders the class tracker page with a list of prefixes and users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered class tracker page.
    """
    prefixes = [
        "ABRK", "ACCT", "ADMF", "AGRI", "ALTF", "AMSL", "ANTH", "AOLS", "APHY", "ARAB",
        "ARTH", "ARTS", "ASTR", "AUBR", "AUTI", "AVIM", "AVIT", "BCOM", "BCOT", "BCTI",
        "BIOL", "BIOT", "BOAT", "BUSI", "BUSN", "CARD", "CATX", "CHEM", "CHIN", "CIMG",
        "CINS", "COMM", "CONT", "CPIN", "CPTR", "CRIM", "CSCI", "CSIA", "CSTC", "DBMS",
        "DENT", "DESN", "DHYG", "DMSI", "ECED", "ECON", "EDSN", "EDUC", "EECT", "EETC",
        "ENGL", "ENGR", "ENGT", "ENRG", "ENTR", "EPCS", "ESOL", "EXER", "FREN", "GENS",
        "GEOG", "GEOL", "GERM", "GLOB", "GRDN", "HIMT", "HIST", "HLHS", "HOSP", "HPER",
        "HSPS", "HUMA", "HUMS", "HVAC", "INDT", "INFM", "ITSP", "IVYC", "IVYT", "LEGS",
        "LIBA", "LOGM", "MAMO", "MATH", "MEAS", "MEDL", "MEMS", "METC", "MKTG", "MORT",
        "MPRO", "MRIT", "MRTC", "MTTC", "NANO", "NETI", "NGAS", "NRSG", "OPTI", "PAET",
        "PARA", "PARM", "PHAR", "PHIL", "PHLB", "PHOT", "PHYS", "PLAS", "POLS", "PPTC",
        "PRCM", "PROC", "PSYC", "PTAS", "QUAL", "RADT", "RDTH", "RESP", "SCIN", "SDEV",
        "SMDI", "SOCI", "SPAN", "SPED", "SURG", "SUST", "SVAD", "TMAS", "TRCK", "VIDT",
        "VISC", "WELD"
    ]

    users = UserInformation.objects.all()
    
    return render(request, 'class_tracker.html', {'prefixes': prefixes, 'users': users})


def search_course(request):
    """
    Searches for a course based on user input and saves it to the database.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered result page or course not found page.
    """
    # Set maximum number of skills per class
    MAX_SKILLS_PER_CLASS = 10

    # If form submitted
    if request.method == 'POST':
        # Get user from form submission
        user_id = request.POST.get('user')
        user = get_object_or_404(UserInformation, pk=user_id)

        # Get course prefix and number from form submission
        prefix = request.POST.get('prefix')
        class_number = request.POST.get('class_number')

        # Scrape course data
        course_data = scrape_course_data(f"{prefix} {class_number}")

        # If course not found
        if course_data is None or not all(course_data):
            return render(request, 'course_not_found.html')

        # Initialize course variables
        course_number, course_name, course_description = course_data

        # Add course to database
        course, course_created = Course.objects.get_or_create(
            course_number=course_number,
            defaults={'name': course_name, 'description': course_description}
        )

        # Add course to user's courses
        user_course, user_course_created = UserCourse.objects.get_or_create(user=user, course=course)

        # Extract skills from course description
        extracted_skills = generate_skills_from_description(course_description)

        # Loop through extracted skills and add them to the database
        for skill_name in extracted_skills:
            # If course already has max number of skills, stop adding skills
            if CourseSkill.objects.filter(course_number=course).count() >= MAX_SKILLS_PER_CLASS:
                break

            # Add skill to database, link skill to course
            skill_instance, _ = Skill.objects.get_or_create(skill_keyword=skill_name)
            course_skill, _ = CourseSkill.objects.get_or_create(course_number=course, skills_id=skill_instance)

        return render(request, 'result.html', {'course': course})
    
    return render(request, 'index.html')