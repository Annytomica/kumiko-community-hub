from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Stores single About Us content entry
    This model has no foreign key 
    Entries can only be submitted by superuser via /admin
    """
    opening = models.CharField(max_length=200)
    body = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.opening
