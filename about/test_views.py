from django.test import TestCase
from django.urls import reverse
from .models import About


"""
Tests for About view

The test sets up a mock About instance for testing

The tests check that page renders correctly by assessing:
- view responds successfully with 200 status
- view displays correct content
- view uses correct template
NB: checking template from Medium article by Alice Campkin
"""


class TestAboutView(TestCase):

    def setUp(self):
        # Create About content for testing

        self.about_us = About(
            opening="This is the opening",
            body="This is body content",
            profile_image="best_image.jpg",
        )

        self.about_us.save()

    def test_render_about_page(self):
        response = self.client.get(reverse('about'))
        # test view responds successfully with ok 200 status
        self.assertEqual(response.status_code, 200)
        # Test that view displays correct content from the 'About' instance
        self.assertIn(b"This is the opening", response.content)
        self.assertIn(b"This is body content", response.content)
        self.assertIn(b"best_image.jpg", response.content)
        # Test that view uses correct template
        self.assertTemplateUsed(response, 'about/about.html')
