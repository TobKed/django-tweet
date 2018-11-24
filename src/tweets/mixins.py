from django import forms
from django.forms.utils import ErrorList


class FormUserNeededMixin:
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super().form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["Ups. You have to be logged sweetheart."])
            return self.form_invalid(form)
