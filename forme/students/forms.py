from dataclasses import field
from django import forms
from .models import *


class Logreg(forms.ModelForm):
    class Meta:
        model = regis
        fields = ['username', 'f_name', 'l_name', 'age', 'email', 'password', 'confirm', 'gender']
