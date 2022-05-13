from rest_framework import serializers
from EmplyeeApp.models import Departments, Employees

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                  'DepartmentName',
        )

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = (
            'EmployeeId',
            'EmployeeName',
            'Department',
            'DateofJoining',
            
        )

