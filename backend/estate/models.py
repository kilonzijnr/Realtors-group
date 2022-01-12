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
    cost = models.CharField(max_length=100)
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


class Comment(models.Model):
    post = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created',)
        
        def __str__(self):
            return 'Comment by {} on {}'.format(self.name, self.post)