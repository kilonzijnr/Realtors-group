from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(property, on_delete=models.CASCADE)
    review = models.TextField(null=True)
    rate_property = models.PositiveSmallIntegerField(choices = RATE_CHOICES)
    
    def no_of_ratings(self):
        ratings = Rating.objects.filter(project=self)
        return len(ratings)

    

def __str__(self):
        return self.user.username
