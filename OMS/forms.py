from django import forms
from django.forms import ModelForm, Textarea, TextInput
from .models import Patient

class NewPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['fname', 'lname', 'gender', 'birthday', 'street', 'phone', 'email', 'street', 'city', 'state', 'zipcode', 'notes']
        widgets = {
            'fname' : TextInput(attrs={'class':'form-control'}),
            'lname' : TextInput(attrs={'class':'form-control'})
        }
