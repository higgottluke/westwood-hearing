from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select, EmailInput, DateInput
from .models import Patient, Audiogram
from django.http import HttpRequest

standardreq = {'class':'form-control', 'required':"", 'autocomplete':"off"}
standard = {'class':'form-control', 'autocomplete':"off"}

class PatientForm(forms.ModelForm):
    class Meta:

        model = Patient
        fields = ['fname', 'lname', 'gender', 'birthday', 'phone', 'email', 'street', 'city', 'state', 'zipcode', 'notes', ]
        widgets = {
            'fname' : TextInput(attrs=standardreq),
            'lname' : TextInput(attrs=standardreq),
            'gender': Select(attrs=standardreq),
            'birthday': DateInput(attrs={'class':'form-control', 'required':"", 'autocomplete':"off"}),
            'email': EmailInput(attrs=standard),
            'street': TextInput(attrs=standard),
            'phone': TextInput(attrs={'class': 'form-control', 'number':'true', 'minlength':'10', 'maxlength':'10'}),
            'city': TextInput(attrs=standard),
            'state': TextInput(attrs={'class': 'form-control', 'minlength':'2', 'maxlength':'2'}),
            'zipcode': TextInput(attrs={'class': 'form-control', 'minlength':'5', 'maxlength':'5', 'number':'true'}),
            'notes': Textarea(attrs={'class': 'form-control autoExpand', 'rows':'2', 'data-min-rows':'2'}),
        }
    label_suffix = ''

class AudiogramForm(forms.ModelForm):
    class Meta:
        model = Audiogram
        fields = '__all__'
        widgets = {
            '__all__': TextInput(standardreq),
        }

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'})

    )
