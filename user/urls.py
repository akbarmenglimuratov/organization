from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', views.ProfileViewSet, basename = 'user-profile-view')

urlpatterns = [
	path('login/', views.CustomAuthToken.as_view(), name = "api_token_auth"),
] + router.urls