from rest_framework import serializers
from profile_api_app.models import Profile, Achievement, Student
from rest_framework.response import Response
from django.contrib.auth.models import User


# NOTE: Use ModelSerializer since we are working with models. If we use serializers.Serializer we just get 200 response

# Profile Serializer takes into account the user's name email and area of interest
class ProfileSerializer(serializers.ModelSerializer):
    # the argument thats passed in serializermethodfield should be a method like it should be a function
    username_field = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Profile
        fields = ['id', 'date_joined', 'first_name', 'last_name', 'email', 'area_of_interest', 'username_field']

    # Basically we are passing in the object and here in this case would be the users profile
    def get_username(self, profile):
        username = profile.user.username
        return username


# Achievement Serializer records the users achievements
class AchievementSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('username_collector')

    class Meta:
        model = Achievement
        fields = ['id', 'date_added', 'achievement_response', 'achievement_pictures', 'user', 'username']

    def username_collector(self, achievement_obj):
        username = achievement_obj.user.username
        return username


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


