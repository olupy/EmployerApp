from rest_framework import serializers
from EmplyeeApp.models import Departments, Employees

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('')

