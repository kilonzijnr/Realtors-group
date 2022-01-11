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

    def save_category(self):
        """
        class method to save category
        """
        self.save()
    def delete_category(self):
        self.delete()
        
class Property(models.Model):
    """[property class]

    Args:
        models ([class]): [Model Class to create property table]]
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="property_images/")
    cost = models.TextField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    contact_info = models.IntegerField(null=True, default=0)

    def __str__(self):
        """[return a stringified version of the object]
        """
        return self.name
    
