from django import forms

from recipes.recipes_app.models import Recipe


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')
        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)',
        }


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')
        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)',
        }


class DeleteRecipeForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')
        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)',
        }
