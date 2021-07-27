from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Profile, Achievement, Student
from .serializer import ProfileSerializer, AchievementSerializer, StudentSerializer, RegisterSerializer
from rest_framework.pagination import PageNumberPagination


# Create your APIview here.
class ShowAllProfile(generics.ListAPIView):
    """
    List all the user profile
        * The user's first and last name
        * Their email and area of interest
        * also the time when they joined + their username
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

    # Post request will handle posting info like first, last name etc
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.first_name = request.data.first_name
            serializer.last_name = request.data.last_name
            serializer.email = request.data.email
            serializer.area_of_interest = request.data.area_of_interest
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)





class ShowAllAchievements(generics.ListCreateAPIView):
    """
    List all the user achievements
        * achievement response with their username

    Allows Post Method to this endpoint
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


class ShowAchievements(APIView):
    """
    Shows a specific user achievement

    This api will handle post request* Handles posting achievement response

    """





