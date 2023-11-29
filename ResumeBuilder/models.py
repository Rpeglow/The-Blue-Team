from django.conf import settings
from django.db import models
from django.utils import timezone
from UserInfo.models import UserInformation
from ClassTracker.models import Course
from ClassTracker.models import Skill

class WorkHistory(models.Model):
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    work_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.company_name}'
    
class Education(models.Model):
    school_name = models.CharField(max_length=100)
    school_state = models.CharField(max_length=100)
    school_city = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    school_start_date = models.DateTimeField()
    school_end_date = models.DateTimeField()
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)

        
        
def __str__(self):
    return f'{self.school_name}, {self.degree}'


#class PopulateKeywords(models.Model):
#   skill_keyword = models.ForeignKey(Skill, on_delete=models.CASCADE)
        