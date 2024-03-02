from .models import *
from django import forms


class EnContactModelForm(forms.ModelForm):
    class Meta:
        model=EnContact
        fields='__all__'