from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Subject

@receiver(post_save, sender=Subject)
def log_subject_creation(sender, instance, created, **kwargs):
    if created:
        print(f"New subject created: {instance.name}")
