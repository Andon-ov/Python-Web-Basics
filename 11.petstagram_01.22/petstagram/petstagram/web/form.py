import datetime
from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from petstagram.web.models import Profile, Pet, PetPhoto
from petstagram.web.views.helpers import BootstrapFormMixin, DisabledFieldsFormMixin


class CreatProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile

        fields = ('first_name', 'last_name', 'picture')

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'picture': 'Link to Profile Picture',
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={  # 'class': 'form-control',
                    'placeholder': 'Enter first name'
                }
            ),

            'last_name': forms.TextInput(
                attrs={  # 'class': 'form-control',
                    'placeholder': 'Enter last name'
                }
            ),

            'picture': forms.TextInput(
                attrs={  # 'class': 'form-control',
                    'placeholder': 'Enter URL'
                }
            )
        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW

    class Meta:
        model = Profile

        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'picture': 'Link to Profile Picture',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
            'picture': forms.TextInput(attrs={'placeholder': 'Enter URL'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description', 'rows': 3, }),
            'date_of_birth': forms.DateInput(attrs={'min': '1920-01-01'}),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')

        labels = {
            'name': 'Pet Name',
            'type': 'Type',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Enter pet name'}), }


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth < self.MIN_DATE_OF_BIRTH or date_of_birth > self.MAX_DATE_OF_BIRTH:
            raise ValidationError(
                f'Date of birth must be between {self.MIN_DATE_OF_BIRTH} and {self.MAX_DATE_OF_BIRTH}')
        return date_of_birth

    class Meta:
        model = Pet
        exclude = ('user_profile',)


class DeletePetForm(DisabledFieldsFormMixin, BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        exclude = ('user_profile',)


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = '__all__'


class EditPhotoForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = '__all__'
