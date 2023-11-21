from django.db import models

class UserInformation(models.Model):
    """
    Represents user information.

    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        middle_initial (str, optional): The middle initial of the user.
        address (str): The address of the user.
        city (str): The city of the user.
        state (str): The state of the user.
        zip_code (str): The zip code of the user.
        phone (str): The phone number of the user.
        email (str): The email address of the user.
        tagline (str): The tagline of the user.

    Methods:
        __str__(): Returns a string representation of the user information.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    tagline = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
