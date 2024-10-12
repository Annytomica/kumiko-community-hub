from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Contact(models.Model):
    """ 
    Stores single about me content
    """
    opening = models.CharField(max_length=200)
    body = models.TextField()
    contact_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.opening


class ContactMessage(models.Model):
    """
    Stores a single contact request message
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Message from {self.name} on {self.created_on}"