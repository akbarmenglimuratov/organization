from rest_framework import serializers
from .models import Organization, Department, Employee

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'
		read_only_fields = ['organization_id']

	def create(self, validated_data):
		obj, created = Employee.objects.update_or_create(
			fio = validated_data['fio'],
			organization_id = validated_data['organization_id'],
			defaults = {**validated_data})
		return obj

class DepartmentDetailSerializer(serializers.ModelSerializer):
	department_employee = EmployeeSerializer(many=True, read_only = True)
	employee_count = serializers.SerializerMethodField()

	def get_employee_count(self, obj):
		queryset = Employee.objects.filter(organization_id=obj.organization_id, department_id = obj)
		return queryset.count()
	class Meta:
		model = Department
		fields = '__all__'
		read_only_fields = ['organization_id']

class OrganizationSerializer(serializers.ModelSerializer):

	organizations_department = DepartmentDetailSerializer(many = True)
	no_department_employees = serializers.SerializerMethodField()

	def get_no_department_employees(self, obj):
		queryset = Employee.objects.filter(organization_id = obj, department_id=None)
		serializer = EmployeeSerializer(queryset, many=True)
		return serializer.data

	class Meta:
		model = Organization
		fields = '__all__'

