from django import forms
from .models import ContactMessage


class ContactMessage(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'message',)