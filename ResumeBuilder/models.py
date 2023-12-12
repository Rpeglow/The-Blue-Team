from django.conf import settings
from django.db import models
from django.utils import timezone
from UserInfo.models import UserInformation
from ClassTracker.models import Course
from ClassTracker.models import Skill, CourseSkill, UserCourse
from django.core import validators

# Creates structure of information being passed to the database from the Work History Section
class WorkHistory(models.Model):
    """
    Represents a work history in the ResumeBuilder system.

    Attributes:
        user (ForeignKey): The user.
        job_title (CharField): The job title for the entry.
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
    job_title = models.CharField(max_length=100, blank=True)
    company_name = models.CharField(max_length=100)
    work_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=15, validators=[validators.RegexValidator(regex=r'^\d{5}(?:-\d{4})?$', message='Zip code must be in the format XXXXX or XXXXX-XXXX')])
    phone = models.CharField(max_length=20, validators=[validators.RegexValidator(regex=r'^\d{3}-\d{3}-\d{4}$', message='Phone number must be in the format XXX-XXX-XXXX')])
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.user}, {self.company_name}, {self.job_title}' 
    
# Creates structure of information being passed to the database from the Education Section
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
    school_end_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
       
    def __str__(self):
        return f'{self.user}, {self.school_name}, {self.degree}'
        
