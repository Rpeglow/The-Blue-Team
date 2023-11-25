from django.conf import settings
from django.db import models
from django.utils import timezone

class Image(models.Model):
    image_url = models.URLField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

