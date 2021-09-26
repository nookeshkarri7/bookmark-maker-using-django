from django import forms
from bookmarkmakerapp.models import bookmarkMakertable

class bookmarkMakerForm(forms.ModelForm):
    site_url=forms.CharField()
    class Meta:
        model=bookmarkMakertable
        fields="__all__"

    
    