from django import forms

from games_play_app.web.models import ProfileModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('email', 'age', 'password')
        # labels = {
        #     'first_name': 'First Name',
        #     'last_name': 'Last name',
        #     'image_url': 'Image URL'
        # }
        #
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
        #     'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
        #     'image_url': forms.TextInput(attrs={'placeholder': 'URL'}),
        # }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

