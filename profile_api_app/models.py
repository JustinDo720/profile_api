from django.db import models
from django.contrib.auth.models import User


# Lets make the Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=75)
    email = models.EmailField(max_length=200)
    area_of_interest = models.TextField(max_length=300)


