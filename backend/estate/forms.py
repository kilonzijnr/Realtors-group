from django import forms
from .models import  Rating, RATE_CHOICES

class RateForm(forms.ModelForm):
    rate_price = forms.ChoiceField(choices=RATE_CHOICES, widget = forms.Select(), required = True)
    rate_location = forms.ChoiceField(choices=RATE_CHOICES, widget = forms.Select(), required = True)
    rate_condition = forms.ChoiceField(choices=RATE_CHOICES, widget = forms.Select(), required = True)

    class Meta:
        model = Rating
        fields = ['rate_price', 'rate_location', 'rate_condition' ]
