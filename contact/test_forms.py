from django.test import TestCase
from .forms import ContactMessage


"""
Tests for contact message form.

The tests check for:
- form vaild when all fields entered correctly
- form invlaid if a field is left empty
- form invalid if a field is whitespace
- form invalid if email is not a valid email address
- form widgets work as expected:
    - placeholders are correct
    - text area for message is 6 rows
NB: ChatGPT was used to help design tests for widgets
"""


class TestContactMessageForm(TestCase):
    # test for checking function when all fields have valid data
    def test_form_valid_with_all_fields(self):
        form = ContactMessage({
            'name': 'Name Entered',
            'email': 'name.entered@email.com',
            'message': 'This form has all fields filled correctly'
        })
        self.assertTrue(
            form.is_valid(),
            msg='Form should be valid when all fields are filled correctly.'
        )

    # tests for checking from invalid when a field is missing data
    def test_form_invalid_without_name(self):
        form = ContactMessage({
            'name': '',
            'email': 'name.entered@email.com',
            'message': 'This form is not filled correctly'
        })
        self.assertFalse(
            form.is_valid(),
            msg='Form should be invalid when name missing.'
        )

    def test_form_invalid_without_email(self):
        form = ContactMessage({
            'name': 'Name Entered',
            'email': '',
            'message': 'This form is not filled correctly'
        })
        self.assertFalse(
            form.is_valid(),
            msg='Form should be invalid when email missing.'
        )

    def test_form_invalid_without_message(self):
        form = ContactMessage({
            'name': 'Name Entered',
            'email': 'name.entered@email.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg='Form should be invalid when no message.'
        )

    # tests for checking form invalid when a field has whitespace
    def test_form_invalid_with_name_whitespace(self):
        form = ContactMessage({
            'name': ' ',
            'email': 'name.entered@email.com',
            'message': 'This form is not filled correctly'
        })
        self.assertFalse(
            form.is_valid(),
            msg='Form should be invalid when name has whitespace.'
        )

    def test_form_invalid_with_email_whitespace(self):
        form = ContactMessage({
            'name': 'Name Entered',
            'email': ' ',
            'message': 'This form is not filled correctly'
        })
        self.assertFalse(
            form.is_valid(),
            msg='Form should be invalid when email whitespace.'
        )

    def test_form_invalid_with_message_whitespace(self):
        form = ContactMessage({
            'name': 'Name Entered',
            'email': 'name.entered@email.com',
            'message': ' '
        })
        self.assertFalse(
            form.is_valid(),
            msg='Form should be invalid when message is whitespace.'
        )

    # test for checking function when email is not valid email address
    def test_form_invalid_with_email_wrong(self):
        form = ContactMessage({
            'name': 'Name Entered',
            'email': 'name.entered.not.email',
            'message': 'This form has email that is incorrect'
        })
        self.assertFalse(
            form.is_valid(),
            msg='Form should be invalid when email is not valid email address.'
        )

    # tests for checking field placeholders are correct
    def test_name_field_placeholder(self):
        form = ContactMessage()
        name_placeholder = form.fields['name'].widget.attrs.get('placeholder')
        self.assertEqual(
            name_placeholder,
            'Name',
            msg="The 'name' field should have the placeholder 'Name'."
        )

    def test_email_field_placeholder(self):
        form = ContactMessage()
        email_placeholder = form.fields['email'].widget.attrs.get(
            'placeholder'
        )
        self.assertEqual(
            email_placeholder,
            'Email',
            msg="The 'email' field should have the placeholder 'Email'."
        )

    def test_message_field_placeholder(self):
        form = ContactMessage()
        message_placeholder = form.fields['message'].widget.attrs.get(
            'placeholder'
        )
        self.assertEqual(
            message_placeholder,
            'Your message here',
            msg=(
                "The 'message' field should have the placeholder"
                "'Your message here'."
            )
        )

    # test for checking message text area has 6 rows
    def test_message_field_rows(self):
        form = ContactMessage()
        message_rows = form.fields['message'].widget.attrs.get('rows')
        self.assertEqual(
            message_rows,
            6,
            msg="The 'message' field should have 6 rows."
        )
