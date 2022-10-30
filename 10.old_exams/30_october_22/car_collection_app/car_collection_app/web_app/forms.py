from django import forms

from car_collection_app.web_app.models import Profile, Car


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile

        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileEditeForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Car.objects.all().delete()
        return self.instance


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')


class CarCreateForm(CarBaseForm):
    pass


class CarEditeForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __disabled_fields(self):
        for _, field in self.fields.items():
            field.disabled = True
