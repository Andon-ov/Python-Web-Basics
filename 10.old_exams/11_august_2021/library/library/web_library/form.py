from django import forms

from library.web_library.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        # labels = {
        #     'first_name': 'First Name',
        #     'last_name': 'Last name',
        #     'image_url': 'Image URL'
        # }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        # labels = {
        #     'first_name': 'First Name',
        #     'last_name': 'Last name',
        #     'image_url': 'Image URL'
        # }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        # labels = {
        #     'first_name': 'First Name',
        #     'last_name': 'Last name',
        #     'image_url': 'Image URL'
        # }


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')
        # labels = {
        #     'first_name': 'First Name',
        #     'last_name': 'Last name',
        #     'image_url': 'Image URL'
        # }


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')
        # labels = {
        #     'first_name': 'First Name',
        #     'last_name': 'Last name',
        #     'image_url': 'Image URL'
        # }


class DeleteBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')
        # labels = {
        #     'first_name': 'First Name',
        #     'last_name': 'Last name',
        #     'image_url': 'Image URL'
        # }
