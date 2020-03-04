from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('employees/', views.EmployeeDetailList .as_view()),
    path('employees/<int:pk>/', views.EmployeeDetailDetail .as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)