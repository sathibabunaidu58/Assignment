from django import forms
from django.forms import forms, ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class Enter(ModelForm):
    
    class Meta:
        model = Details
        fields = ['faculty_name','department']
        