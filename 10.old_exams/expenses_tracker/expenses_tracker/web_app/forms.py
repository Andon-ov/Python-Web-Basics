import os

from django import forms

from expenses_tracker.web_app.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Profile Image',
        }


class EditeProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Profile Image',
        }


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        if self.instance.profile_image:
            os.remove(self.instance.profile_image.path)

        self.instance.delete()
        Expense.objects.all().delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()


# Expenses

class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')
        labels = {
            'expense_image': 'Link to Image',
        }


class EditeExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')
        labels = {
            'expense_image': 'Link to Image',
        }


class DeleteExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = '__all__'
