from django import forms
from .models import Sound


class BlenderForm(forms.Form):
    sounds = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sounds'].choices = Sound.objects.values_list('pk', 'sign')