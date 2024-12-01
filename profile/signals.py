from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from profile.models import Profile


@receiver(post_save, sender=User)
def callback(sender, instance, created, **kwargs):
    if instance:
        Profile.objects.create(user=instance)