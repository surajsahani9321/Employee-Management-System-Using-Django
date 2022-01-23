from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee

        fields = ['name', 'fatherName', 'age', 'dob', 'department', 'address', 'phone', 'email', 'password', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'fatherName': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),

        }
