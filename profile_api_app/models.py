from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Lets make the Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=75)
    email = models.EmailField(max_length=200, null=True, default=None)
    area_of_interest = models.TextField(max_length=300, null=True, default=None)

    def __str__(self):
        return self.user.username


# Achievements Model: Any achievements like honors, groups or scholarships
class Achievement(models.Model):
    # We are always going to start to tie these models to our User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    achievement_response = models.TextField(max_length=500)
    # achievement pictures will be sent to media so keep in mind that you'll need a media folder in project
    achievement_pictures = models.ImageField(default=None, upload_to='achievement_pictures/', blank=True)

    def __str__(self):
        return self.achievement_response[:50]


# Student Profile: Grades, Volunteer/Clubs and activities
class Student(models.Model):
    # Again we are always going to start to tie these models to our User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    overall_gpa = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    activity_title = models.CharField(max_length=100)
    activity_details = models.TextField(max_length=500)
    activity_picture = models.ImageField(default=None, upload_to='activity_picture/', blank=True)

    def __str__(self):
        return f'{self.user.username}: GPA({self.overall_gpa}) and Activity Details {self.activity_details[:50]}'

