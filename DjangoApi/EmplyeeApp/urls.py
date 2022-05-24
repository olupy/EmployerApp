from django.urls import path

from EmplyeeApp import views

urlpatterns = [
    path('department/', views.departmentApi),
    path('department/<int:id>', views.departmentApi),
]

