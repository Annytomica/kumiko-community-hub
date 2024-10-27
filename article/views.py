from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Article, ArticleComment, ArticleLike
from .forms import ArticleCommentForm, ArticleLikeForm


# Class-based view for article list
class ArticleList(generic.ListView):
    """
    View to display a list of published articles with pagination.

    **Models**
    Uses :model:`article.Article` to retrieve and display a list of articles.

    **Context**
    ``article_list``
        A queryset of :model:`article.Article`
        ordered by the most recent creation date
        filtered to only include published articles (status=1).
    ``article.article_likes_count``
        A count of all likes associated with each article in the queryset.
        Calculated dynamically for each article.
    ``article.article_comment_count``
        A count of all approved comments associated with each article
        in the queryset.
        Calculated dynamically for each article.

    **Additional Behavior:**
    Uses pagination to limit the number of articles displayed per page.
    The number of articles displayed per page is set to 8.

    **Template:**
    :template:`article/index.html`
    """
    queryset = Article.objects.filter(status=1).order_by("-created_on")
    template_name = "article/index.html"
    paginate_by = 8

    def get_context_data(self):
        """
        Add like and comment counts for each article to the context.
        """
        # Get the existing context
        context = super().get_context_data()

        # Add like and comment counts for each article
        for article in context['article_list']:
            article.article_likes_count = (
                article.article_like.filter(like=True).count()
            )
            article.article_comment_count = (
                article.article_comments.filter(approved=True).count()
            )

        return context


# Function-based view for a single article
def single_article(request, slug):
    """
    View to display a single article with all features including:
    - single article content
    - like button and like count
    - comments, comment form and comment count
    - next and previous articles navigation

    ** Models **
    Display an individual :model:`article.Article`.
    Interact with :model:`article.ArticleComment` for comment handling.
    Interact with :model:`article.ArticleLike` for like/unlike functionality.

    **Context**
    ``post``
        An instance of :model:`article.Article`.
    ``article_comments``
        All comments related to the article, ordered by creation date.
    `` article_comment_count``
        A count of all approved comments related to the article
    `` article_comment_form``
        An instance of :form:`ArticleCommentForm` used to submit new comments
    ``article_like_count``
        A count of all likes of the article
    ``user_like``
        An instance of :model:`article.ArticleLike`
        if the present user has liked the article, otherwise `None`.
    `` article_like_form``
        An instance of :form:`article_like_form`
        toggles likes via hidden input
    ``next_article``
        An instance of the next :model:`article.Article`
        according to created_on date order or `None` if no next article exists.
    ``prev_article``
        An instance of the previous :model:`article.Article`
        according to created_on date order or
        `None` if no previous article exists.

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
        user_like = (
            ArticleLike.objects.filter(author=request.user, post=post).first()
        )

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
                    # If user already liked the article, toggle the like/unlike
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
                    like = article_like_form.save(commit=False)
                    like.author = request.user
                    like.post = post
                    like.like = True
                    like.save()
                    messages.add_message(request, messages.SUCCESS,
                                         'You liked this article.')

        # Update like button status and recalculate like count after submission
        article_likes_count = post.article_like.filter(like=True).count()
        user_like = (
            ArticleLike.objects.filter(author=request.user, post=post).first()
        )

    # Forms to pass to the template
    article_comment_form = ArticleCommentForm()
    article_like_form = ArticleLikeForm()

    # Get next and previous articles
    next_article = (
        Article.objects.filter(
            status=1,
            created_on__gt=post.created_on
        )
        .order_by('created_on')
        .first()
    )
    prev_article = (
        Article.objects.filter(
            status=1,
            created_on__lt=post.created_on
        )
        .order_by('-created_on')
        .first()
    )

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
         "next_article": next_article,
         "prev_article": prev_article,
         },
    )


# This view was taken from CI blog walkthrough with only minor alteration
def article_comment_edit(request, slug, comment_id):
    """
    View to allow user to edit their own comment on an article.
    Displays an individual comment for edit in comment form.
    A user must be logged in for this view to be present.

    **Models**
    Uses :model:`article.Article` to retrieve the article
    associated with the comment.
    Uses :model:`article.ArticleComment` to retrieve and update the comment.

    **Context**
    ``post``
        An instance of :model:`article.Article`
    ``comment``
        A single comment related to the post
    ``comment_form``
        An instance of :form:`article.ArticleCommentForm`

    **Parameters**
    ``slug``
        A string value used to identify and fetch the relevant article.
    ``comment_id``
        An integer ID used to locate the specific comment to be edited.

    **Template:**
    :template:`article/single_article.html`
    Redirects back to single_article.html (single article view)
    after processing

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


# This view was taken from CI blog walkthrough with only minor alteration
def article_comment_delete(request, slug, comment_id):
    """
    View to allow user to delete their own comment on an article.
    A user must be logged in for this view to be present.

    **Models**
    Uses :model:`article.Article` to retrieve the article
    associated with the comment.
    Uses :model:`article.ArticleComment` to locate and delete the comment.

    **Context**
    ``post``
        An instance of :model:`article.Article`
    ``comment``
        A single comment related to the post

    **Parameters**
    ``slug``
        A string value used to identify and fetch the relevant article.
    ``comment_id``
        An integer ID used to locate the specific comment to be edited.

    **Template:**
    :template:`article/single_article.html`
    Redirects back to single_article.html (single article view)
    after processing
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
