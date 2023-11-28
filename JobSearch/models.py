from django.db import models
from UserInfo.models import UserInformation

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    job_name = models.TextField()
    salary_range = models.TextField()
    description = models.TextField()
    hyperlink = models.TextField()
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.job_name}"

