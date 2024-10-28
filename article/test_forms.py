from django.test import TestCase
from .forms import ArticleCommentForm, ArticleLikeForm


# Tests for Article comment form
class TestArticleCommentForm(TestCase):

    def test_form_is_valid_if_message(self):
        comment_form = ArticleCommentForm({'body': 'This article is awesome'})
        self.assertTrue(
            comment_form.is_valid(),
            msg='Form invalid when filled'
        )

    def test_form_is_invalid_if_empty(self):
        comment_form = ArticleCommentForm({'body': ''})
        self.assertFalse(
            comment_form.is_valid(),
            msg='Form valid when empty'
        )

    def test_form_invalid_if_whitespace_only(self):
        comment_form = ArticleCommentForm({'body': ' '})
        self.assertFalse(
            comment_form.is_valid(),
            msg='Form valid when whitespace'
        )

    def test_form_has_correct_placeholder(self):
        form = ArticleCommentForm()
        placeholder = form.fields['body'].widget.attrs.get('placeholder')
        self.assertEqual(
            placeholder,
            'Leave your comment here',
            msg='Textarea should have correct placeholder'
        )


# Tests for Article Likes form - Like is a Boolean Field
class TestArticleLikeForm(TestCase):

    def test_like_form_is_valid_with_true(self):
        like_form = ArticleLikeForm({'like': True})
        self.assertTrue(
            like_form.is_valid(),
            msg='Form should be valid when like is True'
        )

    def test_like_form_is_valid_with_false(self):
        like_form = ArticleLikeForm({'like': False})
        self.assertTrue(
            like_form.is_valid(),
            msg='Form should be valid when like is False'
        )

    def test_like_form_is_valid_with_initial_none(self):
        # Before first like, default for like should be None
        like_form = ArticleLikeForm({'like': None})
        self.assertTrue(
            like_form.is_valid(),
            msg='Form should be valid when initial like default is None'
        )
