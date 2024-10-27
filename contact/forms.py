from django import forms
from crispy_forms.helper import FormHelper
from .models import ContactMessage


class ContactMessage(forms.ModelForm):
    """
    A form for submitting contact messages via the Contact page.

    **Model**
    Uses :model:`contact.ContactMessage` to create and save messages sent by users.

    **Fields**
    ``name``
        A CharField that captures the name of the person sending the message.
    ``email``
        An EmailField that collects the sender's email address. 
    ``message``
        A TextField that contains the message sent by the user.

    **Widgets**
    `name`: Configured as a `TextInput` widget with a placeholder "Name". 
        This allows users to easily identify where to input their name.
    `email`: Configured as a `TextInput` widget with a placeholder "Email". 
        Helps users identify the field for entering their email address. 
    `message`: Configured as a `Textarea` widget with a placeholder "Your message here" and 6 rows.
        Defining 6 rows creates enough space for users to write detailed messages
        The placeholder helps users identify the field for entering their message

    **Usage**
    This form is used on the contact page to collect messages or inquiries from visitors.
    The widgets enhance user experience by providing visual cues (placeholders) and appropriate field sizes,
    making it easier for users to understand what information they need to enter.
    """
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'message',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', }),
            'email': forms.TextInput(attrs={'placeholder': 'Email', }),
            'message': forms.Textarea(attrs={'rows': 6, 'placeholder':
                                             'Your message here', }),
        }
