from django.db import models
from django.core import validators

class UserInformation(models.Model):
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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
