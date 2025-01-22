from django import forms
from .models import ReadEntry

class ReadEntryForm(forms.ModelForm):
    class Meta:
        model = ReadEntry
        fields = ['title', 'author', 'category', 'status', 'total_pages', 'pages_read', 'image']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'total_pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'pages_read': forms.NumberInput(attrs={'class': 'form-control'}),
        }
