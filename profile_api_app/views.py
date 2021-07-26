from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, Achievement, Student
from .serializer import ProfileSerializer, AchievementSerializer, StudentSerializer, RegisterSerializer


# Create your APIview here.
class ShowAllProfile(APIView):
    """
    List all the user profile
        * The user's first and last name
        * Their email and area of interest
        * also the time when they joined + their username
    """

    # Show Profile will only handle get request. When the user registers the signals will take care of profile creation
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ShowProfile(APIView):
    """
    Shows a specific user profile
    """


class ShowAllAchievements(APIView):
    """
    List all the user achievements
        * achievement response with their username
    """

    # Show all achievements from everyone
    def get(self, request):
        achievements = Achievement.objects.all()
        serializer = AchievementSerializer(achievements, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = AchievementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # if the serializer is saved then the item is created
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # if the serializer failed to save then the item is not created
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ShowAchievements(APIView):
    """
    Shows a specific user achievement

    This api will handle post request* Handles posting achievement response

    """





