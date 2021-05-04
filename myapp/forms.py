from django import forms
from myapp.models import *

class MedForm(forms.ModelForm):
    class Meta:
        model = Med
        fields = '__all__'
