from distutils.command.upload import upload
from django import forms

class browse(forms.Form):
    file = forms.FileField()