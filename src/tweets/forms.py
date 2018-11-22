from django import forms
from .models import Tweet


class TweetModelForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = "__all__"

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if content == "pupa":
            raise forms.ValidationError("Cannot be pupa")
        return content
