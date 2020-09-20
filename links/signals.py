from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Link)
def create_link_detail(sender, instance, created, **kwargs):
    if created:
        LinkDetail.objects.create(link=instance)
