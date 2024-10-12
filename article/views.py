from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Article, ArticleComment, ArticleLike
from .forms import ArticleCommentForm, ArticleLikeForm


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
    
    ``article_comment``
        All comments related to the article
    
    `` article_comment_count``
        A count of all approved comments to the article
    
    ``article_likes``
        All likes related to the article
    
    ``article_like_count``
        A count of all likes of the article

    **Template:**

    :template:`article/single_article.html`
    """

    queryset = Article.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    article_comments = post.article_comments.all().order_by("-created_on")
    article_comment_count = post.article_comments.filter(approved=True).count()
    article_likes = post.article_like.all().order_by("-created_on")
    article_likes_count = post.article_like.all().count()
    
    if request.method == "POST":
        article_comment_form = ArticleCommentForm(data=request.POST)
        if article_comment_form.is_valid():
            comment = article_comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
        
        article_like_form = ArticleLikeForm(data=request.POST)
        if article_like_form.is_valid():
            like = article_like_form.save(commit=False)
            like.author = request.user
            like.post = post
            like.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    
    article_comment_form = ArticleCommentForm()
    article_like_form = ArticleLikeForm()

    return render(
        request,
        "article/single_article.html",
        {"article": post,
        "article_comments": article_comments,
        "article_comment_count": article_comment_count,
        "article_comment_form": article_comment_form,
        "article_likes": article_likes,
        "article_likes_count": article_likes_count,
        "article_like_form": article_like_form,
        },
    )


def article_comment_edit(request, slug, comment_id):
    """
    view to edit article comments
    """
    if request.method == "POST":

        queryset = Article.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(ArticleComment, pk=comment_id)
        comment_form = ArticleCommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('single_article', args=[slug]))


def article_comment_delete(request, slug, comment_id):
    """
    view to delete article comments
    """
    queryset = Article.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(ArticleComment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment Deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'Nope, that was not your comment to delete!')

    return HttpResponseRedirect(reverse('single_article', args=[slug]))