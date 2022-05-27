
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
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

@csrf_exempt
def employeeApi(request,id=0):
    if request.method == "GET":
        employees = Employees.objects.all()
        employees_serializers = EmployeeSerializers(employees, many = True)
        return JsonResponse(employees_serializers.data, safe = False)

    elif request.method == "POST":
        employees_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializers(data = employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("saved successfully!", safe= False)
        return JsonResponse("failed to add!",safe= False)

    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId = employee_data["EmployeeId"])
        employee_serializer = EmployeeSerializers(employee, data = employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("updated successfully", safe = False)
        return JsonResponse("an Error occured in updating", safe = False)

    elif request.method == "DELETE":
        employee = Employees.objects.get(EmployeeId = id)
        employee.delete()
        return JsonResponse("Deleted Successfully", safe = False)

@csrf_exempt
def saveFile(request):
    file = request.FILES["myfile"]
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)