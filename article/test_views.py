from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .forms import ArticleCommentForm, ArticleLikeForm
from .models import Article, ArticleLike, ArticleComment


"""
Tests for Article List view

The test sets up:
- a mock superuser instance
- a mock list of published articles
- a single unpublished article instance

The tests check that page renders correctly by assessing:
- view responds successfully with 200 status
- view uses correct template
- View pagination works correctly
- view does not display unpublished article
- view displays published article content
- view displays article like and comment counts

NB: ChatGPT was used to help design tests for:
- pagination
- like and comment counts

NB: checking template from Medium article by Alice Campkin

"""


class TestArticleListView(TestCase):
    def setUp(self):
        # create user profile
        self.user = User.objects.create_superuser(
            username="superuser",
            password="superPassword",
            email="superuser@email.com"
        )

        # create list of published mock articles
        for i in range(12):
            Article.objects.create(
                title=f"Test Article {i}",
                slug=f"Test-Article-{i}",
                author=self.user,
                content="Test content",
                excerpt="Test excerpt",
                pull_quote=f"Test quote {i}",
                primary_image="test_image.jpeg",
                tags=1,
                status=1,
            )

        # create instance of unpublished article
        Article.objects.create(
            title="Unpublished Test Article",
            slug="Unpublished-Test-Article",
            author=self.user,
            content="Test content",
            excerpt="Test excerpt",
            pull_quote="Unpublished Test Quote",
            primary_image="test_image.jpeg",
            tags=1,
            status=0,
            )

    # test that ArticleList view renders correctly
    def test_render_article_list_page(self):
        response = self.client.get(reverse('home'))
        # test view responds successfully with ok 200 status
        self.assertEqual(response.status_code, 200)
        # Test that view uses correct template
        self.assertTemplateUsed(response, 'article/index.html')
        # Test pagination is working correctly
        self.assertEqual(len(response.context['article_list']), 8)
        # Test unpublished article not displayed
        self.assertNotIn(b"Unpublished Test Article", response.content)
        # Test that view displays correct content from the 'Article' instance
        self.assertIn(b"Test Article", response.content)
        self.assertIn(b"Test-Article", response.content)
        self.assertIn(b"Test excerpt", response.content)
        self.assertIn(b"test_image.jpeg", response.content)
        # test that like and comment counts displayed correctly
        for article in response.context['article_list']:
            self.assertTrue(hasattr(article, 'article_likes_count'))
            self.assertTrue(hasattr(article, 'article_comment_count'))


"""
Tests for single article view

The test sets up:
- two mock user instances
- a single published article instance
- an approved article comment by user
- an unapproved article comment by user
- an unapproved article comment by user2
- an article like by user

The tests check that:
1. page renders correctly by assessing:
- view responds successfully with 200 status
- view uses correct template
- view displays published article content
- view displays approved article comments
- view displays comments and like forms
- view displays comments and like counts

2. when a user is logged in:
- view displays unapproved comment if by logged in user
- view displays unapproved comment by another user but
comment is hidden by `d-none` class
- use can like and unlike an article
- user can submit a comment
- user can edit and delete a comment

NB: ChatGPT was used to help design tests for:
- comments, especially unapproved comment by another user
- like/unlike testing
- testing login status
NB: Comment submission test modified from CI Blog walkthrough
NB: checking template from Medium article by Alice Campkin

"""


class TestSingleArticleView(TestCase):
    def setUp(self):
        # create user profile
        self.user = User.objects.create_user(
            username="superuser",
            password="superPassword",
            email="superuser@email.com"
        )
        self.user.save()

        # create second user profile
        self.user2 = User.objects.create_user(
            username="seconduser",
            password="secondPassword",
            email="seconduser@email.com"
        )
        self.user2.save()

        # create instance of published article
        self.article = Article(
            title="Test Article",
            slug="Test-Article",
            author=self.user,
            content="Test content",
            excerpt="Test excerpt",
            pull_quote="Test Quote",
            primary_image="test_image.jpeg",
            tags=1,
            status=1,
            )
        self.article.save()

        # create instance of approved article comment
        self.comment1 = ArticleComment(
            post=self.article,
            author=self.user,
            body="This is an approved comment",
            approved=True,
        )
        self.comment1.save()

        # create instance of unapproved article comment by user
        self.comment2 = ArticleComment(
            post=self.article,
            author=self.user,
            body="This is an unapproved comment",
            approved=False,
        )
        self.comment2.save()

        # create instance of unapproved article comment by user2
        self.comment3 = ArticleComment(
            post=self.article,
            author=self.user2,
            body="This is an unapproved comment by user2",
            approved=False,
        )
        self.comment3.save()

    # test that single article view renders correctly
    def test_render_single_article_page(self):
        # access article view
        response = self.client.get(
            reverse('single_article', args=[self.article.slug]))
        # test view responds successfully with ok 200 status
        self.assertEqual(response.status_code, 200)
        # Test that view uses correct template
        self.assertTemplateUsed(response, 'article/single_article.html')
        # Test that view displays correct content from the 'Article' instance
        self.assertIn(b"Test Article", response.content)
        self.assertIn(b"Test content", response.content)
        self.assertIn(b"Test excerpt", response.content)
        self.assertIn(b"Test Quote", response.content)
        self.assertIn(b"test_image.jpeg", response.content)
        # test approve comment displayed
        self.assertContains(response, self.comment1.body)
        # test comment form displayed
        self.assertIsInstance(
            response.context['article_comment_form'], ArticleCommentForm)
        # test like form displayed
        self.assertIsInstance(
            response.context['article_like_form'], ArticleLikeForm)
        # test likes and comment counts displayed
        self.assertIn('article_likes_count', response.context)
        self.assertIn('article_comment_count', response.context)

    """
    Tests for comment functionality

    """
    def test_unapproved_comment_display_status(self):
        # login as user (not user2) and check logged in parameters
        logged_in = self.client.login(
            username="superuser",
            password="superPassword"
        )
        self.assertTrue(self.user.check_password("superPassword"))
        self.assertTrue(logged_in, "Login failed in test")

        if logged_in:
            # access article view
            response = self.client.get(
                reverse('single_article', args=[self.article.slug]))
            # test unapproved comment by user is displayed
            self.assertContains(response, self.comment2.body)
            # test unapproved comment by user2 is displayed
            self.assertContains(response, self.comment3.body)
            # test unapproved comment by user2 is hidden using `d-none` class
            self.assertContains(response, 'd-none')
            self.assertNotContains(
                response,
                f'<li class="depth-1 comment faded">{self.comment3.body}'
            )

    def test_successful_comment_submission(self):
        # submit comment as test user
        self.client.force_login(self.user)
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(
            reverse("single_article", args=[self.article.slug]),
            post_data
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )

    """
    Tests for Like and Unlike functionality

    """
    def test_like_count_and_user_like_status(self):
        # Like the article as the test user
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("single_article", args=[self.article.slug]),
            {"like": True},  # Submitting a like via the form
        )
        article = Article.objects.get(id=self.article.id)
        like_count = article.article_like.filter(like=True).count()

        # Check that like count is correct and user has liked the article
        self.assertEqual(like_count, 1)
        self.assertTrue(
            ArticleLike.objects.filter(
                post=article,
                author=self.user,
                like=True
            )
            .exists()
        )

    def test_unlike_functionality(self):
        # Like the article first
        self.client.force_login(self.user)
        self.client.post(reverse(
            "single_article", args=[self.article.slug]), {"like": True})

        # Unlike the article
        response = self.client.post(
            reverse("single_article", args=[self.article.slug]),
            {"like": True},  # Toggle the like off
        )
        article = Article.objects.get(id=self.article.id)
        like_count = article.article_like.filter(like=True).count()

        # Check that like count is correct and user has unliked the article
        self.assertEqual(like_count, 0)
        self.assertFalse(
            ArticleLike.objects.filter(
                post=article,
                author=self.user,
                like=True
            )
            .exists()
        )

    """
    Test article_comment_edit and article_comment_delete views

    Uses mock data from single article view test setup

    tests that comments can:
    - not be edited or deleted by a user who did not generate the comment
    - be edited or deleted by user who generated the comment

    """

    def test_only_author_can_edit_comment(self):
        # attempt to edit when not correct user - should not work
        self.client.force_login(self.user2)
        response = self.client.post(
            reverse("article_comment_edit",
                    args=[self.article.slug, self.comment1.id]
                    ),
            {"body": "Edited comment"}
        )
        # Shouldn't change
        self.comment1.refresh_from_db()
        self.assertEqual(self.comment1.body, "This is an approved comment")

        # attempt to edit when correct user - should work
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("article_comment_edit",
                    args=[self.article.slug, self.comment1.id]),
            {"body": "Edited comment"}
        )
        # Should change
        self.comment1.refresh_from_db()
        self.assertEqual(self.comment1.body, "Edited comment")

    def test_only_author_can_delete_comment(self):
        # attempt to delete when not correct user - should not work
        self.client.force_login(self.user2)
        response = self.client.post(
            reverse("article_comment_delete",
                    args=[self.article.slug, self.comment1.id])
        )
        # Should not delete
        self.assertTrue(
            ArticleComment.objects.filter(id=self.comment1.id).exists())

        # attempt to delete when correct user - should work
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("article_comment_delete",
                    args=[self.article.slug, self.comment1.id])
        )
        # Should delete
        self.assertFalse(
            ArticleComment.objects.filter(id=self.comment1.id).exists())
