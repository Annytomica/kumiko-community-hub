from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class About(models.Model):
    opening = models.CharField(max_length=200)
    body = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.opening