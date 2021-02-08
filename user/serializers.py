from rest_framework import serializers
from django.contrib.auth.models import User
from .models import OrganizationUser

class ExtraSerializer(serializers.ModelSerializer):

	class Meta:
		model = OrganizationUser
		fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
	organization_user = ExtraSerializer()
	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'organization_user']