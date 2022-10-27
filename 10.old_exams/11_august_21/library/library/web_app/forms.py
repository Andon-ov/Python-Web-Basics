from django import forms

from library.web_app.models import Profile, Book


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'URL'})
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditeForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Book.objects.all().delete()
        return self.instance


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image': forms.TextInput(attrs={'placeholder': 'Image'}),
            'type': forms.TextInput(attrs={'placeholder': 'Faction, Novel, Crime..'}),
        }


class BookCreateForm(BookBaseForm):
    pass


class BookEditeForm(BookBaseForm):
    pass


class BookDeleteForm(BookBaseForm):
    class Meta:
        model = Book
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
