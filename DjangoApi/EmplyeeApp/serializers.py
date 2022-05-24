from rest_framework import serializers
from EmplyeeApp.models import Departments, Employees

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                  'Department_Name',
        )

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = (
            'EmployeeId',
            'EmployeeName',
            'Department',
            'DateofJoining',
            'PhotoFileName',
        )

