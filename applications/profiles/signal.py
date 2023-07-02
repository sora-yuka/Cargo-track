from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

from applications.profiles.models import ShipperProfile, DriverProfile, CompanyProfile
User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ShipperProfile.objects.create(user=instance)
        DriverProfile.objects.create(user=instance)
        CompanyProfile.objects.create(user=instance)