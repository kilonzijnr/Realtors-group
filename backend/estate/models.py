from django.db import models

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    review = models.TextField(null=True)
    rate_property = models.PositiveSmallIntegerField(choices = RATE_CHOICES)
    
