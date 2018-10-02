import hashlib
import io

from PIL import Image
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.forms import forms, CharField, IntegerField, ImageField, URLField


# Noe tull
class ArticleForm(forms.Form):
    title = CharField(max_length=120)
    #Required has to be False, because i did not find a way that i could edit an article without uplouding an image again.
    header_image = ImageField(required=False)

    text = CharField()

    #Check if the things that is written in the form are valid
    def clean(self):
        return self.cleaned_data

        #try:
        #    if self.cleaned_data["description"].startswith(" "):
        #        raise ValidationError({'name': "Input cannot start with a space"}, code='invalid')
        #except KeyError:
        #    raise ValidationError({'name': "Description must be provided"}, code='invalid')
        #return self.cleaned_data

