# Django Rest Framework Library
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Django Models and Seriallizers
from account.models import EmployeeDetail
from .serializers import EmployeeDetailSerializer

class EmployeeDetailList(APIView):
    """
    List all EmployeeDetails, or create a new EmployeeDetail.
    """
    def get(self, request, format=None):
        employeeDetails = EmployeeDetail.objects.all()
        serializer = EmployeeDetailSerializer(employeeDetails, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailDetail(APIView):
    """
    Retrieve, update or delete a EmployeeDetail instance.
    """
    def get_object(self, pk):
        try:
            return EmployeeDetail.objects.get(pk=pk)
        except EmployeeDetail.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employeeDetail = self.get_object(pk)
        serializer = EmployeeDetailSerializer(employeeDetail)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employeeDetail = self.get_object(pk)
        serializer = EmployeeDetailSerializer(employeeDetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employeeDetail = self.get_object(pk)
        employeeDetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)