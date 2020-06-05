from django import forms
from .models import TaskModel

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskModelForm(forms.ModelForm):
    class Meta:
        model  = TaskModel
        fields = {
            'title',
            'description',
            'due_date',
            'user_choice',
        }
        widgets={
            'due_date':DateInput()
        }
        labels = {
            'title':"Title",
            'description':"Description",
            'due_date':"Due Date",
            'user_choice':"Task Type",
        }
