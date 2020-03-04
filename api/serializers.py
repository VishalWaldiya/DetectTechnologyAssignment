from rest_framework import serializers
from account.models import EmployeeDetail

class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetail
        fields = '__all__'