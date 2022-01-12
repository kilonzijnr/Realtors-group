from django.db import models

# Create your models here.
category_choices = (
    ("HOUSE", "House"),
    ("LAND", "Land"),
    ("APARTMENT", "Apartment"),
)

  
class Property(models.Model):
    """[property class]

    Args:
        models ([class]): [Model Class to create property table]]
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="property_images/")
    cost = models.IntegerField(null=True,default=0)
    property_type = models.CharField(max_length=50, choices = category_choices)
    date_created = models.DateField(auto_now_add=True)
    contact_info = models.IntegerField(null=True, default=0)

    def __str__(self):
        """[return a stringified version of the object]
        """
        return self.name
    
    def save_property(self):
        """
        class method to save property
        """
        self.save()
    @property
    def number_of_properties(self):
        """[return total number of properties]
        """
        return Property.objects.filter(property=self).count()


