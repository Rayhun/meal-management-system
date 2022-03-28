from dataclasses import fields
from django import forms

# local import
from meal.models import Deposet


class DeposetForm(forms.ModelForm):
    """ Deposet Form """
    class Meta:
        model = Deposet
        fields = ['amount']
