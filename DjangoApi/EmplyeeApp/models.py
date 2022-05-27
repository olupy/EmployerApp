from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    Department_Name = models.CharField(max_length=200)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key= True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length= 100)
    DateofJoining = models.DateField(max_length=100)
    PhotoFileName = models.CharField(max_length=100)



