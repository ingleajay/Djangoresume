from django.db import models
from django.contrib.auth.models import AbstractUser


class ResumeUser(AbstractUser):
    COUNTRY_CHOICE = (
        ('india', 'india'),
        ('japan', 'japan'),
        ('china', 'china'),
    )
    GENDER_CHOICE = (
        ('male', 'male'),
        ('female', 'female'),
    )
    city = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to="media/%y")
    country = models.CharField(
        choices=COUNTRY_CHOICE, max_length=50, blank=True, null=True, default="india")
    gender = models.CharField(
        choices=GENDER_CHOICE, max_length=50, blank=True, null=True, default="male")
