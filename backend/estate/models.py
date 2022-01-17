from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    image = models.ImageField(default='default.png',upload_to='profile_images')

    def __str__(self):
        return f'{self.customer.username}-Profile'

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
    cost = models.CharField(max_length=100)
    property_type = models.CharField(max_length=50, choices = category_choices)
    date_created = models.DateField(auto_now_add=True)
    contact_info = models.IntegerField(null=True, default=0)
    image1 = models.ImageField(upload_to="property_images/",default='default.jpeg')
    image2 = models.ImageField(upload_to="property_images/",default='default.jpeg')
    image3 = models.ImageField(upload_to="property_images/",default='default.jpeg')
    

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

class Comments(models.Model):
    
    
    comment = models.CharField(max_length=60)

    @classmethod
    def display_comments(cls):
        return cls.objects.all()

    def save_comments(self):
        self.save()
    def __str__(self):
        return self.comment