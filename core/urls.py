from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('detail', views.OrganizationViewSet, basename='organization-view')
router.register('employee', views.EmployeeViewSet, basename='employee-view')
router.register('department', views.OrganizationDepartmentViewSet, basename='organization-department-view')

urlpatterns = router.urls