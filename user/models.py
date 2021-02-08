from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import secrets
from core.models import Organization

class OrganizationUser(models.Model):

	user = models.OneToOneField(
		User, 
		on_delete = models.CASCADE, 
		related_name = "organization_user")
	organization_id = models.ForeignKey(
		Organization, 
		on_delete = models.SET_NULL, 
		related_name = "organization_id", 
		null=True, blank=True)
	api_key = models.CharField(max_length = 255)

@receiver(post_save, sender=User, dispatch_uid="create_profile")
def update_profile(sender, instance, **kwargs):
	if kwargs["created"]:
		user_data = OrganizationUser.objects.create(user=instance)
		user_data.api_key = secrets.token_urlsafe(16)
		user_data.save()