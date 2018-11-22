from django import forms
from .models import Tweet


class TweetModelForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["content"]

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if content == "bad word":
            raise forms.ValidationError("Cannot be bad word")
        return content
