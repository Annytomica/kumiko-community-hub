from django import forms
from crispy_forms.helper import FormHelper
from .models import ContactMessage


class ContactMessage(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'message',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', }),
            'email': forms.TextInput(attrs={'placeholder': 'Email', }),
            'message': forms.Textarea(attrs={'rows': 6, 'placeholder':
                                             'Your message here', }),
        }
