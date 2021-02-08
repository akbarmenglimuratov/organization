from rest_framework import permissions
from user.models import OrganizationUser

# class OrganizationUserAccessPermission(permissions.BasePermission):
# 	message = 'No access!'

# 	def has_permission(self, request, view):
# 		if request.user.is_authenticated:
# 			# return (request.GET.get('api_key',None) == request.user.company_admin.api_key)
# 			return True
# 		return False
class UserHasCompanyPermission(permissions.BasePermission):
	message = "User has no company!"

	def has_permission(self, request, view):
		if request.user.is_authenticated:
			return bool(request.user.organization_user.organization_id is not None)
		return False