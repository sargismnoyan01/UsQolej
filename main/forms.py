from .models import *
from django import forms


class ContactModelForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'