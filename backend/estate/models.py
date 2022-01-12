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

    def average_ratings(self):
        sum = 0
        ratings = Rating.objects.filter(project=self)
        for rating in ratings:
            sum += ((rating.rate_design + rating.rate_usability + rating.rate_content)/3)
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0


def __str__(self):
        return self.user.username
