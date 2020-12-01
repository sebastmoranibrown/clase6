from django import forms

class CheckedForm(forms.Form):
    checked = forms.BooleanField()
    