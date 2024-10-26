from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import ContactMessage


# Create your views here.
def contact_me(request):
    """
    Renders the most recent information about the website
    and allows user feedback
    Displays an individual instance of :model:`contact.Contact`.

    **Context**
    ``contact``
        The most recent instance of :model:`contact.Contact`.
    ``contact_message``
        An instance of :form`contact.ContactMessage`.

    **Template**
    :template:`contact/contact.html`
    """

    if request.method == "POST":
        contact_message = ContactMessage(data=request.POST)
        if contact_message.is_valid():
            contact_message.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Message sent! Thank You!")

    """
    Renders the Contact page
    """
    contact = Contact.objects.all().order_by('-updated_on').first()

    contact_message = ContactMessage()

    return render(
        request,
        "contact/contact.html",
        {"contact": contact,
         "contact_message": contact_message, },
    )
