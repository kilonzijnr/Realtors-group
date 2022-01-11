from django.db import models

# Create your models here.
category_choices = (
    ("HOUSE", "house"),
    ("LAND", "land"),
    ("APARTMENT", "apartment"),
)
class PropertyType(models.Model):
    """[Property type model]

    Args:
        models ([type]): [Type of property model]
    """
    name = models.CharField(max_length=50, choices = category_choices)