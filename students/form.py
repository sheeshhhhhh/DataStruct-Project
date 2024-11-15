from django.forms import ModelForm, widgets
from django import forms
from .models import Students

class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = ['stdId', 'stdName', 'stdYear', 'stdCourse']

        widgets = {
            'stdId': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Student ID'
            }),
            'stdName': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Student Name'
            }),
            'stdYear': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Student Year'
            }),
            'stdCourse': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Student Course'
            })
        }
        
