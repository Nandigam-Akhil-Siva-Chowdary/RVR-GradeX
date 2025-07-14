from django import forms
from .models import StudentRecord

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentRecord
        fields = [
            'name', 'reg_number', 'branch', 'calculation_type', 
            'sgpa', 'sem1_gpa', 'sem2_gpa', 'cgpa'
        ]
        widgets = {
            'calculation_type': forms.HiddenInput(),
            'sgpa': forms.HiddenInput(),
            'cgpa': forms.HiddenInput(),
        }
