from django.shortcuts import render
from api.serializers import EmployeeSerializer
from rest_framework import viewsets
from api.models import Employees


# Create your views here.

class Employeeviewset(viewsets.ModelViewSet):
    queryset=Employees.objects.all()
    serializer_class=EmployeeSerializer
