from rest_framework import serializers
from profile_api_app.models import Profile, Achievement, Student
from rest_framework.response import Response
from django.contrib.auth.models import User


# NOTE: Use ModelSerializer since we are working with models. If we use serializers.Serializer we just get 200 response

# Profile Serializer takes into account the user's name email and area of interest
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


# Achievement Serializer records the users achievements
class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = "__all__"


# Student Serializer records the user's student status like their grades and activities
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


# Register Serializer is going to be used to register our users so
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
