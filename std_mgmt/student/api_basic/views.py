from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Student, University
from .serializers import StudentSerializer, UniversitySerializer
from django.views.decorators.csrf import csrf_exempt  
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class UniversityAPIView(APIView):
    def get(self,request):
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many = True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = UniversitySerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
class UniversityDetails(APIView):
    def get_object(self,id):
        try:
            return University.objects.get(id = id)
        except University.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
            
    def get(self, request, id):
        university = self.get_object(id)
        serializer = UniversitySerializer(university)
        return Response(serializer.data)
        
    def put(self, request, id):
        university = self.get_object(id)
        serializer = UniversitySerializer(university, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, id):
        university = self.get_object(id)
        university.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)





class StudentAPIView(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
class StudentDetails(APIView):
    def get_object(self,id):
        try:
            return Student.objects.get(id = id)
        except Student.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
            
    def get(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
        
    def put(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, id):
        student = self.get_object(id)
        student.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)