from this import d
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmplyeeApp.models import Departments, Employees
from EmplyeeApp.serializers import EmployeeSerializers, DepartmentSerializers

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method == "GET":
        departments = Departments.objects.all()
        departments_serializers = DepartmentSerializers(departments, many = True)
        return JsonResponse(departments_serializers.data, safe = False)

    elif request.method == "POST":
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializers(data = department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("saved successfully!", safe= False)
        return JsonResponse("failed to add!",safe= False)

    elif request.method == "PUT":
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        department_serializer = DepartmentSerializers(department, data = department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("updated successfully", safe = False)
        return JsonResponse("an Error occured in updating", safe = False)

    elif request.method == "DELETE":
        department = Departments.objects.get(DepartmentId = id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe = False)

