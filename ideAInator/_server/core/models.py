from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone

# Create your models here.

class myUser(AbstractUser):
    conversations = models.JSONField(default=list, blank=True)
    classes = models.JSONField(default=list, blank=True)
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )

  
class PDFUpload(models.Model):
    user = models.ForeignKey(myUser, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='pdfs/')
    upload_date = models.DateTimeField(auto_now_add=True)
    file_description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.display_name}'s PDF - {self.file_description or 'No Description'}"

class ChatLog(models.Model):
    user = models.ForeignKey(myUser, on_delete=models.CASCADE)  
    content = models.TextField(default="chat")  # This will store the chat content
    timestamp = models.DateTimeField(default=timezone.now)  # This will store the timestamp

    
    def __str__(self):
        return f"Chat by {self.user.display_name} on {self.timestamp}"

class ExtractedText(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    text = models.TextField()  # Field to store the extracted text
    class_name = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation

    def __str__(self):
        return f"ExtractedText {self.id} created on {self.created_at}"