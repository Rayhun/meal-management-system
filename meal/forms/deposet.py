from dataclasses import fields
from django import forms

# local import
from meal.models import Deposet


class DeposetForm(forms.ModelForm):
    """ Deposet Form """
    class Meta:
        model = Deposet
        fields = ['amount']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': "Please Enter Your Amount"
            }
        )
