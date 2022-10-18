from django import forms

from recipes.web_app.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')
        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)',
        }


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')
        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)',
        }


class DeleteRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')
        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
