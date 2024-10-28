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
                title = f"Test Article {i}",
                slug = f"Test-Article-{i}",
                author = self.user,
                content = "Test content",
                excerpt = "Test excerpt",
                pull_quote = f"Test quote {i}",
                primary_image = "test_image.jpeg",
                tags = 1,
                status = 1,
            )

        # create instance of unpublished article
        Article.objects.create(
            title = "Unpublished Test Article",
            slug = "Unpublished-Test-Article",
            author = self.user,
            content = "Test content",
            excerpt = "Test excerpt",
            pull_quote = "Unpublished Test Quote",
            primary_image = "test_image.jpeg",
            tags = 1,
            status = 0,
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


class TestSingleArticleView(TestCase):
    def setUp(self):
        # create user profile
        self.user = User.objects.create_superuser(
            username="superuser",
            password="superPassword",
            email="superuser@email.com"
        )

        # create instance of published article
        self.article = Article(
            title = "Test Article",
            slug = "Test-Article",
            author = self.user,
            content = "Test content",
            excerpt = "Test excerpt",
            pull_quote = "Test Quote",
            primary_image = "test_image.jpeg",
            tags = 1,
            status = 1,
            )
        self.article.save()
    
    # test that ArticleList view renders correctly
    def test_render_single_article_page(self):
        response = self.client.get(reverse('single_article', args=[self.article.slug]))
        # test view responds successfully with ok 200 status
        self.assertEqual(response.status_code, 200)
        # Test that view uses correct template
        self.assertTemplateUsed(response, 'article/single_article.html')
        # Test that view displays correct content from the 'Article' instance
        self.assertIn(b"Test Article", response.content)
        #self.assertIn(b"Test-Article", response.content)
        #self.assertIn(b"Test excerpt", response.content)
        #self.assertIn(b"test_image.jpeg", response.content)
        # test that like and comment counts displayed correctly
        #self.assertTrue(hasattr(article, 'article_likes_count'))
        #self.assertTrue(hasattr(article, 'article_comment_count'))