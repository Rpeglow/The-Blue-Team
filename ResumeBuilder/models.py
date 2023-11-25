from django.conf import settings
from django.db import models
from django.utils import timezone
from UserInfo.models import UserInformation
from ClassTracker.models import Course




class WorkHistory(models.Model):
    company_name = models.CharField(max_length=100)
    word_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.company_name}'