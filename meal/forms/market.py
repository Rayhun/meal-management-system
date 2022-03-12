from django import forms

from meal.models.market import Market, Item


class ItemForm(forms.ModelForm):
    """ Form for creating a new item """
    class Meta:
        model = Item
        fields = ['name', 'quantity', 'price']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})


ItemFormSet = forms.modelformset_factory(
    Item, form=ItemForm, extra=1, can_delete=True, validate_min=True
)
