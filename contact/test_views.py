from django.test import TestCase
from django.urls import reverse
from .forms import ContactMessage
from .models import Contact


"""
Tests for Contact view

The test sets up:
- a mock Contact instance for testing
- a mock contact form entry for teseting

The tests check that:
1. page renders correctly by assessing:
- view responds successfully with 200 status
- view displays correct content
- view uses correct template
- contact form renders correctly
NB: checking template from Medium article by Alice Campkin

2. The contact form submits successfully
- form responds successfully with 200 status
- receive correct success message
NB: testing form submission based on CI blog walkthrough
"""


class TestContactView(TestCase):

    def setUp(self):
        # Create Contact content for testing

        self.contact_us = Contact(
            opening="This is the opening",
            body="This is body content",
            contact_image="new_image.jpg",
        )

        self.contact_us.save()

    # test that contact view renders correctly
    def test_render_contact_page(self):
        response = self.client.get(reverse('contact'))
        # test view responds successfully with ok 200 status
        self.assertEqual(response.status_code, 200)
        # Test that view displays correct content from the 'Contact' instance
        self.assertIn(b"This is the opening", response.content)
        self.assertIn(b"This is body content", response.content)
        self.assertIn(b"new_image.jpg", response.content)
        # Test that view uses correct template
        self.assertTemplateUsed(response, 'contact/contact.html')
        # test form renders as expected
        self.assertIsInstance(
            response.context['contact_message'], ContactMessage)

    # test that contact message form submits correctly
    def test_successful_contact_message_sumbission(self):
        # Create Contact form content for testing
        form = {
            'name': 'Name Entered',
            'email': 'name.entered@email.com',
            'message': 'This form has all fields filled correctly'
        }
        response = self.client.post(reverse('contact'), form)
        # test form responds successfully with ok 200 status
        self.assertEqual(response.status_code, 200)
        # test recieve correct success message
        self.assertIn(
            b"Message sent! Thank You!",
            response.content
        )
