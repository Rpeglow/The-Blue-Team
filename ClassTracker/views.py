from django.shortcuts import render, get_object_or_404
from UserInfo.models import UserInformation
from .models import Course, Skill, CourseSkill, UserCourse
from .scraping import scrape_course_data
from .ai import generate_skills_from_description

MAX_SKILLS_PER_CLASS = 10

def index(request):
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
    
    return render(request, 'index.html', {'prefixes': prefixes, 'users': users})


def search_course(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        user = get_object_or_404(UserInformation, pk=user_id)

        prefix = request.POST.get('prefix')
        class_number = request.POST.get('class_number')

        course_data = scrape_course_data(f"{prefix} {class_number}")

        if course_data is None or not all(course_data):
            return render(request, 'course_not_found.html')

        course_number, course_name, course_description = course_data

        course, course_created = Course.objects.get_or_create(
            course_number=course_number,
            defaults={'name': course_name, 'description': course_description}
        )

        user_course, user_course_created = UserCourse.objects.get_or_create(user=user, course=course)

        extracted_skills = generate_skills_from_description(course_description)

        for skill_name in extracted_skills:
                if CourseSkill.objects.filter(course_number=course).count() >= MAX_SKILLS_PER_CLASS:
                    break

                skill_instance, _ = Skill.objects.get_or_create(skill_keyword=skill_name)
                course_skill, _ = CourseSkill.objects.get_or_create(course_number=course, skills_id=skill_instance)

        return render(request, 'result.html', {'course': course})
    
    return render(request, 'index.html')