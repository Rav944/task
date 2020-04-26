from django.db import models

# Create your models here.


class UrlInformation(models.Model):
    original_url = models.TextField(max_length=2000)
    short_version = models.TextField(max_length=2000)
