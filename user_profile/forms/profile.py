from django import forms
from user_profile.models.profile import Profile, Education


class ProfileForm(forms.ModelForm):
    """
    Profile form.
    """
    class Meta:
        model = Profile
        fields = ['dob', 'mobile', 'address', 'profile_pic']

        widgets = {
            'dob': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'mobile': forms.NumberInput(
                attrs={
                    'type': 'number',
                    'class': 'form-control'
                }
            ),
            'address': forms.Textarea(
                attrs={
                    'rows': '3',
                    'class': 'form-control'
                }
            ),
        }


class EducationForm(forms.ModelForm):
    """
    Education form.
    """
    class Meta:
        model = Education
        fields = ['result', 'university', 'start_date', 'end_date', 'description']

        widgets = {
            'result': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Result'
                }
            ),
            'university': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'start_date': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'end_date': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'rows': '3',
                    'class': 'form-control'
                }
            ),
        }


EducationFormSet = forms.modelformset_factory(
    Education, form=EducationForm, extra=1, can_delete=True
)
