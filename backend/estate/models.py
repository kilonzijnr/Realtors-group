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

class Property(models.Model):
    """[property class]

    Args:
        models ([class]): [Model Class to create property table]]
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="property_images/")
    cost = models.TextField(max_length=100)
    
