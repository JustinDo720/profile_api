from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Lets make the Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=75)
    email = models.EmailField(max_length=200, null=True, default=None)
    area_of_interest = models.TextField(max_length=300, null=True, default=None)


# Achievements Model: Any achievements like honors, groups or scholarships
class Achievement(models.Model):
    # We are always going to start to tie these models to our User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement_response = models.TextField(max_length=500)
    # achievement pictures will be sent to media so keep in mind that you'll need a media folder in project
    achievement_pictures = models.ImageField(default=None, upload_to='achievement_pictures/', blank=True)


# Student Profile: Grades, Volunteer/Clubs and activities
class Student(models.Model):
    # Again we are always going to start to tie these models to our User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    overall_gpa = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    activity_title = models.CharField(max_length=100)
    activity_details = models.TextField(max_length=500)
    activity_picture = models.ImageField(default=None, upload_to='activity_picture/', blank=True)