from django import forms

from games_app.web_app.models import Profile, GameModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')

        widgets = {
            'password': forms.PasswordInput()
        }


class EditeProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            GameModel.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class BaseGameModelForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = ('title', 'category', 'rating', 'max_Level', 'image_url', 'summary',)


class CreateGameModelForm(BaseGameModelForm):
    pass


class EditeGameModelForm(BaseGameModelForm):
    pass


class DeleteGameModelForm(BaseGameModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
