from django.db import models
from UserInfo.models import UserInformation

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_number = models.CharField(max_length=50)
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.course_number}"

class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    skill_keyword = models.TextField()

    def __str__(self):
        return f"{self.skill_keyword}"
    
class CourseSkill(models.Model):
    course_number = models.ForeignKey(Course, on_delete=models.CASCADE)
    skills_id = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('course_number', 'skills_id'),)

    def __str__(self):
        return f"{self.course_number} {self.skills_id}"

class UserCourse(models.Model):
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'course'], name='unique_user_course')
        ]

    def __str__(self):
        return f"{self.user} {self.course}"
