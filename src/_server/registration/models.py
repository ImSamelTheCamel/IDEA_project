from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    anumber = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=200)
    edu_person_nickname = models.CharField(max_length=100, null=True, blank=True)

    usu_preferred_email = models.EmailField(null=True, blank=True)
    usu_email_id_address = models.EmailField()
    mail = models.EmailField()

    member_of = models.TextField(null=True, blank=True)
    
    service_name = models.CharField(max_length=255, null=True, blank=True)
    service_description = models.TextField(null=True, blank=True)
    identifier = models.CharField(max_length=255, null=True, blank=True)  # Entity ID
    reply_url = models.URLField(null=True, blank=True)

    classes = models.JSONField(default=list, blank=True)  # List of class names
    conversations = models.JSONField(default=list, blank=True)  # Nested JSON for conversations

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  
        blank=True
    )

    def __str__(self):
        return self.display_name or self.username
