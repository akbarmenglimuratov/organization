from django.contrib import admin
from . import models

@admin.register(models.OrganizationUser)
class CompanyBossesAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'organization_id']