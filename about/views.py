from django.shortcuts import render
from .models import About


# Function-based view for a single about us page
# this view was modified from CI blog walkthrough about/about_me view
def about_me(request):
    """
    View to display content for a single about us page
    Displays the most recent entry in database
 
    ** Models **
    Display an individual instance of :model:`about.About`.

    **Context**
    ``about``
        An instance of :model:`about.About`.

    **Template:**
    :template:`about/about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
