from django import forms

from library.web_library.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        # labels = {
        #     'first_name': 'First Name',
        #     'last_name': 'Last name',
        #     'image_url': 'Image URL'
        # }
