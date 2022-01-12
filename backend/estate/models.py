from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(property, on_delete=models.CASCADE)
    review = models.TextField(null=True)
    rate_property = models.PositiveSmallIntegerField(choices = RATE_CHOICES)
    
