from django.db import models
from UserInfo.models import UserInformation

class Job(models.Model):
    """
    Represents a job in the JobSearch system.

    Attributes:
        id (AutoField): The primary key of the job.
        job_name (TextField): The name of the job.
        salary_range (TextField): The salary range of the job.
        description (TextField): The description of the job.
        hyperlink (TextField): The hyperlink to the job posting.
        user (ForeignKey): The user.

    Methods:
        __str__(): Returns a string representation of the job.
    """

    id = models.AutoField(primary_key=True)
    job_name = models.TextField()
    salary_range = models.TextField()
    description = models.TextField()
    hyperlink = models.TextField()
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}, {self.job_name}"

