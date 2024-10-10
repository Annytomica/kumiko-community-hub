from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article


# Create your views here.
class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1).order_by("-created_on")
    template_name = "article/index.html"
    paginate_by = 1


def single_article(request, slug):
    """
    Display an individual :model:`article.Article`.

    **Context**

    ``post``
        An instance of :model:`article.Article`.

    **Template:**

    :template:`article/single_article.html`
    """

    queryset = Article.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "article/single_article.html",
        {"article": post},
    )