from django import forms
from .models import TrackedFile
from ckeditor.widgets import CKEditorWidget

class FileEditForm(forms.ModelForm):
    class Meta:
        model = TrackedFile
        fields = ['current_content']
        widgets = {
            'current_content': forms.Textarea(attrs={'rows': 10, 'class': 'form-control'}),
        }

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = TrackedFile
        fields = ['name', 'current_content']
        widgets = {
            'current_content': CKEditorWidget()
        }
