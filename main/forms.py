
from django import forms
from django.forms import ModelForm, TextInput

from main.models import NameForm

class ormForm(ModelForm):
    class Meta:
        model = NameForm
        fields = "__all__"
        widgets = {  
            "qw": TextInput(attrs={
             "class":"form-control",
             "placeholder": "имя"
            }),
        }