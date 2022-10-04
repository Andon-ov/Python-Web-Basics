from django import forms

from notes.web_notes.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name',
                  'last_name',
                  'age',
                  'image_url')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': 'Link to Profile Image',
        }


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            # field.widget.attrs['disabled'] = 'disabled'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'




class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            'title',
            'content',
            'image_url'
        )
        labels = {
            'image_url': 'Link to Image',
        }


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            'title',
            'content',
            'image_url'
        )
        labels = {
            'image_url': 'Link to Image',
        }


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            # field.widget.attrs['disabled'] = 'disabled'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = (
            'title',
            'content',
            'image_url'
        )
        labels = {
            'image_url': 'Link to Image',
        }
