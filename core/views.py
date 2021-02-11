from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User

from user.models import OrganizationUser
from core.models import Organization, Department, Employee
from core.serializers import *
from core.permissions import *
import pandas as pd
import json

class IsRegistredUser:

	def get_organization_user(self):
		user = User.objects.get(username = self.request.user)
		return user.organization_user.organization_id

class OrganizationDepartmentViewSet(viewsets.GenericViewSet, IsRegistredUser):
	permission_classes = [UserHasCompanyPermission]
	serializer_class = DepartmentDetailSerializer
	def get_queryset(self):
		self.organ_id = self.get_organization_user()
		queryset = Department.objects.filter(organization_id = self.organ_id)
		return queryset

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(queryset, pk = self.kwargs['pk'])
		return obj

	# GET
	def list(self, request):
		queryset = self.get_queryset()
		department = get_list_or_404(queryset)
		serializer = DepartmentDetailSerializer(department, many = True)
		return Response(serializer.data, status = 200)

	# GET
	def retrieve(self, request, pk):
		department = self.get_object()
		serializer = DepartmentDetailSerializer(department)
		return Response(serializer.data)

	# PATCH
	def partial_update(self, request, pk):
		department = self.get_object()
		serializer = DepartmentDetailSerializer(department, data=request.data)
		if serializer.is_valid():
			serializer.save()
		else:
			return Response({"success":False, "errors":serializer.errors, "data":serializer.data}, status=400)
		return Response({"success":True, "errors":serializer.errors, "data":serializer.data}, status = 202)

	# DELETE
	def destroy(self, request, pk):
		department = self.get_object()
		department.delete()
		return Response({"success": True }, status = 204)

	# POST
	def create(self, request):
		queryset = self.get_queryset()
		serializer = DepartmentDetailSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save(organization_id = self.organ_id)
		else:
			return Response({"success":False, "errors":serializer.errors, "data":serializer.data}, status = 400)
		return Response({"success":True, "errors":serializer.errors, "data":serializer.data}, status=201)


class OrganizationViewSet(viewsets.GenericViewSet, IsRegistredUser):
	permission_classes = [UserHasCompanyPermission]
	
	def get_queryset(self):
		self.organ_id = self.get_organization_user()
		queryset = Organization.objects.all()
		return queryset

	def list(self,request):
		queryset = self.get_queryset()
		organization = get_object_or_404(queryset, pk = self.organ_id.id)
		serializer = OrganizationSerializer(organization)
		context = {
			'title': "Все данные о копмании " + serializer.data['name'],
			'code': 200,
			'message': "Все данные о копмании " + serializer.data['name'],
			'payload': {
				'data': serializer.data,
			}
		}
		return Response(context, status = 200)


class EmployeeViewSet(viewsets.GenericViewSet, IsRegistredUser):
	permission_classes = [UserHasCompanyPermission]

	def get_queryset(self):
		self.organ_id = self.get_organization_user()
		queryset = Employee.objects.filter(organization_id = self.organ_id).order_by('department_id')
		return queryset

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(queryset, pk = self.kwargs['pk'])
		return obj

	def list(self, request):
		queryset = self.get_queryset()
		employee = get_list_or_404(queryset)
		serializer = EmployeeSerializer(employee, many=True)
		return Response(serializer.data, status = 200)

	def retrieve(self, request, pk):
		employee = self.get_object()
		serializer = EmployeeSerializer(employee)
		return Response(serializer.data, status = 200)

	def partial_update(self,request, pk):
		employee = self.get_object()
		serializer = EmployeeSerializer(employee, data=request.data)
		if serializer.is_valid():
			serializer.save(organization_id=self.organ_id)
		else:
			return Response({"success":False, "errors": serializer.errors }, status=400)
		return Response({"success":True, "data": serializer.data }, status=200)

	def create(self,request):
		queryset = self.get_queryset()
		if request.data.get('file', None) is None:
			serializer = EmployeeSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save(organization_id=self.organ_id)
			else:
				return Response({"success":False, "errors": serializer.errors, "data": serializer.data}, status=400)
			return Response({"success":True, "errors":serializer.errors, "data": serializer.data}, status=201)

		file = request.data['file']
		df = pd.read_excel(file)
		json_data = df.to_json(orient='records')
		json_data = json.loads(json_data)
		for data in json_data:
			data['organization_id'] = self.organ_id
			if data['department_id'] is not None:
				department, created = Department.objects.get_or_create(
					name = data['department_id'],
					organization_id = self.organ_id)
				data['department_id'] = department.id
			serializer = EmployeeSerializer(data = data)
			if serializer.is_valid():
				serializer.save(organization_id = self.organ_id)
			else:
				return Response({"success":False, "errors": serializer.errors, "data": serializer.data}, status=400)
		return Response({"success":True, "errors":serializer.errors, "data": {}}, status=201)

	def destroy(self, request, pk):
		employee = self.get_object()
		employee.delete()
		return Response({"success":True, "message":"Successful deleted!", "data": {}}, status = 204)