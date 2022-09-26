from petstagram.web.models import Profile


def get_profile():
    user_profile = Profile.objects.all()
    if user_profile:
        return user_profile[0]
    return None


class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():

            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})

            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'


class DisabledFieldsFormMixin:
    disabled_fields = '__all__'
    fields = {}

    def _init_disabled_fields(self):
        for name, field in self.fields.items():
            if self.disabled_fields != '__all__' and name not in self.disabled_fields:
                continue
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['readonly'] = 'readonly'
            # field.widget.attrs['disabled'] = 'disabled'
