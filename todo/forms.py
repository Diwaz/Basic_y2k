from django import forms
from . import models

class Todo(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ("__all__",)

