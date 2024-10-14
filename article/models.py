from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

TAGS = ((0, "New"), (1, "Course"), (2, "Tools"),
        (3, "Project"), (4, "Wood"), (5, "How-to"), (6, "Book"))
STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Article(models.Model):
    """
    Stores a single article entry related to :model:'auth.User'.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article_posts")
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    pull_quote = models.CharField(max_length=200, unique=True)
    primary_image = CloudinaryField('image', default='placeholder')
    tags = models.IntegerField(choices=TAGS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written on {self.created_on}"


class ArticleComment(models.Model):
    """
    Stores a single comment entry related to :model:'auth.User'
    and :model:'article.Article'.
    """
    post = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="article_comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article_commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.body} by {self.author}"


class ArticleLike(models.Model):
    """
    Stores a single like related to :model:'auth.User'
    and :model:'article.Article'.
    """
    post = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="article_like"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article_liker"
    )
    like = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.like} by {self.author}"
