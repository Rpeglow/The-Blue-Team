from django.contrib import admin
from .models import Course, Skill, CourseSkill, UserCourse

# Register your models here.
admin.site.register(Course)
admin.site.register(Skill)
admin.site.register(CourseSkill)
admin.site.register(UserCourse)
