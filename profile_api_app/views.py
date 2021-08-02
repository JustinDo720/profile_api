from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Profile, Achievement, Student
from .serializer import ProfileSerializer, AchievementSerializer, StudentSerializer, RegisterSerializer
from rest_framework.pagination import PageNumberPagination


# Create your APIview here.

"""
Note:
    * Every Model has two API view that either list EVERY data in the model or ONE data given an id
    * Post request will ONLY be present in the API view that handles EVERY data 
    * Put, Delete will also be present in API views that handle ONE data 
"""


class ShowAllProfile(generics.ListAPIView):
    """
    List all the user profile
        * The user's first and last name
        * Their email and area of interest
        * also the time when they joined + their username

    Show Profile does not need a post request because it is automatically created when a user registers
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = PageNumberPagination


class ShowProfile(APIView):
    """
    Shows a specific user profile
    """

    # Once we put a get method that uses the user_id from urls we could filter Profile for the correct user
    def get(self, request, user_id):
        user_profile = Profile(id=user_id)
        serializer = ProfileSerializer(user_profile, many=False)
        return Response(serializer.data)


class ShowAllAchievements(generics.ListCreateAPIView):
    """
    List all the user achievements
        * achievement response with their username

    Allows Post Method to this endpoint.
        * Users could add their achievements to this endpoint
    """

    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        # first set the serializer
        serializer = AchievementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowAchievement(APIView):
    """
    Shows a specific user achievement

    This api will handle post request* Handles posting achievement response

    """

    def get(self, request, achievement_id):
        achievement = Achievement.objects.get(id=achievement_id)
        serializer = AchievementSerializer(achievement, many=False)
        return Response(serializer.data)


class ShowAllStudents(generics.ListCreateAPIView):
    """
    Shows all the Student information of every user
        * Shows their gpa clubs etc

    This Endpoint will handle Post request.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer(queryset, many=True)
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowStudent(APIView):
    """
    Shows a specific Student information about that user
        * Shows a specific user's student info
    """

    def get(self, request, student_id, *args, **kwargs):
        student = Student.objects.get(id=student_id)
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data)

