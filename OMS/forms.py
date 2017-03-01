from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select, EmailInput, DateInput
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['fname', 'lname', 'gender', 'birthday', 'phone', 'email', 'street', 'city', 'state', 'zipcode', 'notes']
        widgets = {
            'fname' : TextInput(attrs={'class':'form-control', 'required':""}),
            'lname' : TextInput(attrs={'class':'form-control', 'required':""}),
            'gender': Select(attrs={'class': 'form-control', 'required':""}),
            'birthday': TextInput(attrs={'class': 'form-control', 'required':""}),
            'email': EmailInput(attrs={'class':'form-control'}),
            'street': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control', 'number':'true', 'minlength':'10', 'maxlength':'10'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'state': TextInput(attrs={'class': 'form-control', 'minlength':'2', 'maxlength':'2'}),
            'zipcode': TextInput(attrs={'class': 'form-control', 'minlength':'5', 'maxlength':'5', 'number':'true'}),
            'notes': Textarea(attrs={'class': 'form-control autoExpand', 'rows':'2', 'data-min-rows':'2'}),
        }
    label_suffix = ''
