from django import forms

from meal.models.market import ToDo


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
