from django.db import models
from django.core import validators
from django.contrib.auth.models import User

class UserInformation(models.Model):
    """
    Represents user information.

    Attributes:
        id (AutoField): The primary key for the user information.
        first_name (CharField): The first name of the user.
        last_name (CharField): The last name of the user.
        middle_initial (CharField): The middle initial of the user (optional).
        address (CharField): The address of the user.
        city (CharField): The city of the user.
        state (CharField): The state of the user.
        zip_code (CharField): The zip code of the user, validated using a regular expression.
        phone (CharField): The phone number of the user, validated using a regular expression.
        email (EmailField): The email address of the user, validated using an email validator.
        tagline (TextField): The tagline of the user, must be at least 10 characters long.

    Methods:
        __str__(): Returns a string representation of the user information.
    """

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20, validators=[validators.RegexValidator(regex=r'^\d{5}(?:-\d{4})?$', message='Zip code must be in the format XXXXX or XXXXX-XXXX')])
    phone = models.CharField(max_length=20, validators=[validators.RegexValidator(regex=r'^\d{3}-\d{3}-\d{4}$', message='Phone number must be in the format XXX-XXX-XXXX')])
    email = models.EmailField(validators=[validators.EmailValidator()])
    tagline = models.TextField(validators=[validators.MinLengthValidator(10, message='Tagline must be at least 10 characters long.')])
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
