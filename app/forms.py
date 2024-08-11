

from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class LastActiveForm(forms.Form):
    last_active = forms.DateField(widget=DateInput)
