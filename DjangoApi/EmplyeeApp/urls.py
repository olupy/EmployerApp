from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from EmplyeeApp import views

urlpatterns = [
    path('department/', views.departmentApi),
    path('department/<int:id>', views.departmentApi),
    path('employee/', views.employeeApi),
    path('employee/<int:id>', views.employeeApi),
    path('employee/savefile', views.saveFile )
] 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

