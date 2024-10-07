from django.db import models
from django.contrib.auth.models import User

TAGS = ((0, "None"), (1, "Course"), (2, "Tools"), (3, "Project"), (4, "Wood"), (5, "How-to"))
STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="article_posts")
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    pull_quote = models.CharField(max_length=200, unique=True)
    tags = models.IntegerField(choices=TAGS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)