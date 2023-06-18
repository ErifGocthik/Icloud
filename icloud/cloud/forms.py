from django import forms
from django.forms.widgets import TextInput

from cloud.models import Image, Archive


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['id', 'date']


class ArchiveForm(forms.ModelForm):
    class Meta:
        model = Archive
        exclude = ['id',]
