from django.db import models
from UserInfo.models import UserInformation

class Course(models.Model):
    """
    Represents a course in the ClassTracker system.

    Attributes:
        id (AutoField): The primary key of the course.
        course_number (CharField): The course number.
        name (TextField): The name of the course.
        description (TextField): The description of the course.

    Methods:
        __str__(): Returns a string representation of the course.
    """
    id = models.AutoField(primary_key=True)
    course_number = models.CharField(max_length=10)
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.course_number}"

class Skill(models.Model):
    """
    Represents a skill in the ClassTracker system.

    Attributes:
        id (AutoField): The primary key of the skill.
        skill_keyword (TextField): The skill keyword.

    Methods:
        __str__(): Returns a string representation of the skill.
    """
    id = models.AutoField(primary_key=True)
    skill_keyword = models.TextField()

    def __str__(self):
        return f"{self.skill_keyword}"
    
class CourseSkill(models.Model):
    """
    Represents the relationship between a course and a skill in the ClassTracker system.

    Attributes:
        course_number (ForeignKey): The course number.
        skills_id (ForeignKey): The skill id.

    Methods:
        __str__(): Returns a string representation of the course skill.
    """
    course_number = models.ForeignKey(Course, on_delete=models.CASCADE)
    skills_id = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('course_number', 'skills_id'),)

    def __str__(self):
        return f"{self.course_number} {self.skills_id}"

class UserCourse(models.Model):
    """
    Represents the enrollment of a user in a course in the ClassTracker system.

    Attributes:
        user (ForeignKey): The user.
        course (ForeignKey): The course.

    Methods:
        __str__(): Returns a string representation of the user course.
    """
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'course'], name='unique_user_course') # user and course combined has to be unique
        ]

    def __str__(self):
        return f"{self.user} {self.course}"
