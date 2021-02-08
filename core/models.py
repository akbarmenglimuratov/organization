from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):

	name = models.CharField(max_length = 255)
	address = models.CharField(max_length = 255, null = True, blank=True)

	class Meta:
		verbose_name = "Organization"
		verbose_name_plural = "Organizations"

	def __str__(self):
		return self.name

class Department(models.Model):

	name = models.CharField(max_length = 255)
	organization_id = models.ForeignKey(
		Organization,
		on_delete = models.CASCADE, 
		related_name = "organizations_department")

	class Meta:
		verbose_name = "Department"
		verbose_name_plural = "Departments"

	def __str__(self):
		return str(self.id) + "_" + self.name

class Employee(models.Model):

	fio = models.CharField(max_length = 255)
	phone = models.PositiveBigIntegerField(blank=True, null=True)
	organization_id = models.ForeignKey(
		Organization, 
		on_delete = models.CASCADE, 
		related_name = "organization_employee")
	department_id = models.ForeignKey(
		Department, 
		on_delete = models.SET_NULL, 
		related_name = "department_employee",
		null=True,
		blank=True)

	class Meta:
		verbose_name = "Employee"
		verbose_name_plural = "Employees"

	def __str__(self):
		return self.fio