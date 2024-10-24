from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Article, ArticleComment, ArticleLike
from .forms import ArticleCommentForm, ArticleLikeForm


# Create your views here.

# Class-based view for article list
class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1).order_by("-created_on")
    template_name = "article/index.html"
    paginate_by = 8

    def get_context_data(self):
            # Get the existing context
            context = super().get_context_data()
            
            # Add like and comment counts for each article
            for article in context['article_list']:
                article.article_likes_count = article.article_like.filter(like=True).count()
                article.article_comment_count = article.article_comments.filter(approved=True).count()

            return context

# Function-based view for a single article
def single_article(request, slug):
    """
    Display an individual :model:`article.Article`.

    **Context**

    ``post``
        An instance of :model:`article.Article`.

    ``article_comments``
        All comments related to the article

    `` article_comment_count``
        A count of all approved comments to the article

    ``article_like_count``
        A count of all likes of the article
    
    ``user_like``
        The like status of the present user

    **Template:**

    :template:`article/single_article.html`
    """

    # get the article
    queryset = Article.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    # get the comments and likes
    article_comments = post.article_comments.all().order_by("-created_on")
    article_comment_count = post.article_comments.filter(approved=True).count()
    article_likes_count = post.article_like.filter(like=True).count()

    # Check if user already liked post
    user_like = None
    if request.user.is_authenticated:
        user_like = ArticleLike.objects.filter(author=request.user, post=post).first()
        print(user_like)                                      


    if request.method == "POST":
        # comment form
        if 'body' in request.POST:
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

        # like/unlike
        elif 'like' in request.POST:
            article_like_form = ArticleLikeForm(data=request.POST)
            if article_like_form.is_valid():
                if user_like:
                    # If user already liked the article, toggle the like (unlike if liked)
                    print('user_like recognised')
                    user_like.like = not user_like.like
                    user_like.save()
                    if user_like.like:
                        messages.add_message(request, messages.SUCCESS,
                                             'You liked this article.')
                    else:
                        messages.add_message(request, messages.SUCCESS,
                                             'You unliked this article.')

                else:
                    # If user has not liked yet, create a new like
                    print('default else')
                    like = article_like_form.save(commit=False)
                    like.author = request.user
                    like.post = post
                    like.like = True
                    like.save()
                    messages.add_message(request, messages.SUCCESS,
                                         'You liked this article.')

        # Update like button status and recalculate like count after submission
        article_likes_count = post.article_like.filter(like=True).count()
        user_like = ArticleLike.objects.filter(author=request.user, post=post).first()
    
    
    # Forms to pass to the template
    article_comment_form = ArticleCommentForm()
    article_like_form = ArticleLikeForm()

    return render(
        request,
        "article/single_article.html",
        {"article": post,
         "article_comments": article_comments,
         "article_comment_count": article_comment_count,
         "article_comment_form": article_comment_form,
         "article_likes_count": article_likes_count,
         "article_like_form": article_like_form,
         "user_like": user_like,
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
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

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
        messages.add_message(request, messages.ERROR,
                             'Nope, that was not your comment to delete!')

    return HttpResponseRedirect(reverse('single_article', args=[slug]))
