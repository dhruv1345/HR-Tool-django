from django.contrib import admin
from .models import TrackedFile, Version

admin.site.register(TrackedFile)
admin.site.register(Version)

