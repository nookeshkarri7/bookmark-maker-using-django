from django import forms
from bookmarkmakerapp.models import bookmarkMakertable

class bookmarkMakerForm(forms.ModelForm):
    site_url=forms.CharField()
    class Meta:
        model=bookmarkMakertable
        fields="__all__"

    def clean(self):
        cleaned_data=super().clean()
        url=cleaned_data['site_url']
        if url[-4:]!=".com":
            raise forms.ValidationError("Please Enter Valid URL")
        return url
