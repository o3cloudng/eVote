from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, AdminProfile, AgentProfile, CustomerProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == User.Roles.ADMIN:
            AdminProfile.objects.create(user=instance, full_name=instance.email)
        elif instance.role == User.Roles.AGENT:
            AgentProfile.objects.create(user=instance, agency_name="Default Agency", license_number=f"LIC-{instance.id}")
        elif instance.role == User.Roles.USER:
            CustomerProfile.objects.create(user=instance, full_name=instance.email)
