from django.db import models
from cloudinary.models import CloudinaryField


class Contact(models.Model):
    """
    Stores single Contact content entry
    This model has no foreign key
    Entries can only be submitted by superuser via /admin
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
    This model has no foreign key
    Entries can be submitted by any site user - no registration required
    Stored messages are only viewable by site admin via /admin
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
