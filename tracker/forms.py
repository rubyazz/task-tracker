from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-title'}),
            'description': forms.Textarea(attrs={'class': 'form-desc'}),
            'status': forms.Select(attrs={'class': 'form-status'})
        }
