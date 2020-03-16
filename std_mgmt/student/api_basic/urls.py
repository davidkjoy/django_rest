from django.contrib import admin
from django.urls import path
from .views import  UniversityAPIView, UniversityDetails, StudentAPIView, StudentDetails

urlpatterns = [
    path('university/', UniversityAPIView.as_view()),
    path('university_detail/<int:id>/', UniversityDetails.as_view()),
    path('student/', StudentAPIView.as_view()),
    path('student_detail/<int:id>/', StudentDetails.as_view()),

]