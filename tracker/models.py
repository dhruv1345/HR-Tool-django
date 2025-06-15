from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class TrackedFile(models.Model):
    name = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to='uploads/', blank=True, null=True)  # ✅ Add this
    current_content = RichTextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Version(models.Model):
    file = models.ForeignKey(TrackedFile, on_delete=models.CASCADE, related_name='versions')
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} edited by {self.editor.username} on {self.edited_at}"


class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
