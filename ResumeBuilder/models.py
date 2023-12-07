from django.conf import settings
from django.db import models
from django.utils import timezone
from UserInfo.models import UserInformation
from ClassTracker.models import Course
from ClassTracker.models import Skill, CourseSkill, UserCourse

class WorkHistory(models.Model):
    """
    Represents a work history in the ResumeBuilder system.

    Attributes:
        user (ForeignKey): The user.
        company_name (CharField): The company name.
        work_address (CharField): The work address.
        city (CharField): The city.
        state (CharField): The state.
        zip (CharField): The zip code.
        phone (CharField): The phone number.
        start_date (DateField): The start date.
        end_date (DateField): The end date.
    
    Methods:
        __str__(): Returns a string representation of the work history.
    """
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    work_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.company_name 
    
class Education(models.Model):
    """
    Represents an education in the ResumeBuilder system.

    Attributes:
        user (ForeignKey): The user.
        school_name (CharField): The school name.
        school_state (CharField): The school state.
        school_city (CharField): The school city.
        degree (CharField): The degree.
        school_start_date (DateField): The start date.
        school_end_date (DateField): The end date.

    Methods:
        __str__(): Returns a string representation of the education.
    """
    school_name = models.CharField(max_length=100)
    school_state = models.CharField(max_length=100)
    school_city = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    school_start_date = models.DateField()
    school_end_date = models.DateField()
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
       
    def __str__(self):
        return f'{self.school_name}, {self.degree}'