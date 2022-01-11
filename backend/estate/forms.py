from django import forms
from .models import Property,PropertyType


class PropertyForm(forms.ModelForm):
    """[property form class]

    Args:
        forms ([class]): [Class to create a form from the property model]
    """
    class Meta:
        model = Property
        fields = "__all__"