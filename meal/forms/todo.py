from django import forms

from meal.models.market import ToDo


class ToDoForm(forms.ModelForm):
    """ Form for creating a new todo """
    class Meta:
        model = ToDo
        fields = [
            'user', 'name', 'category', 'description', 'start_date',
            'end_date', 'is_completed'
        ]
