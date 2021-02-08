from django.contrib import admin
from . import models

@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'organization_id']
	
@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['id', 'fio', 'organization_id', 'department_id', 'phone']
	