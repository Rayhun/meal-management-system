from django import forms

from meal.models.market import ToDo, NeedItem


class ToDoForm(forms.ModelForm):
    """ Form for creating a new todo """
    class Meta:
        model = ToDo
        fields = [
            'user', 'name', 'category', 'description', 'start_date',
            'end_date'
        ]

        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'rows': '1'
            }),
            'start_date': forms.TextInput(attrs={
                'class': 'form-control', 'type': 'date'
            }),
            'end_date': forms.TextInput(attrs={
                'class': 'form-control', 'type': 'date'
            }),
        }


class NeedItemForm(forms.ModelForm):
    """ Form for creating a new todo """
    class Meta:
        model = NeedItem
        fields = [
            'name', 'quantity', 'date', 'quantity_type'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity_type': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={
                'class': 'form-control', 'type': 'date'
            }),
        }


NeedItemFormSet = forms.modelformset_factory(
    NeedItem, form=NeedItemForm, extra=1, can_delete=True
)
