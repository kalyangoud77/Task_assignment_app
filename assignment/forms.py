from django import forms
from .models import *

class TaskAssignmentForm(forms.ModelForm):
    class Meta:
        model = TaskAssignment
        fields = '__all__'
class DveloperForm(forms.ModelForm):
    class Meta:
        model = Taskdone
        fields = '__all__'
