from django import forms
from bookmarkmakerapp.models import bookmarkMakertable
class bookmarkMakerForm(forms.ModelForm):
    class Meta:
        model=bookmarkMakertable
        fields="__all__"