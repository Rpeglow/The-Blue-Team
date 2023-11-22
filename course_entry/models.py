from django.conf import settings
from django.db import models
from django.utils import timezone

# Based on the database design I have included elements from the user_courses, courses, and course_skills keys
# They will be adjusted in the future
class Course(models.Model):
    course_number = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()

    def __str__(self):
        return self.course_number + self.course_name + self.course_description
    
class Skill(models.Model):
    skill_id = models.IntegerField()
    skill_keyword = models.CharField(max_length=100)
    
    def __str__(self):
        return self.skill_id + self.skill_keyword
    
class Image(models.Model):
    image_url = models.URLField()
    description = models.CharField(max_length=255)
    
