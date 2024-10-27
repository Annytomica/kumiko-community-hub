from django.urls import path
from . import views

# URL pattern for the about us page
urlpatterns = [
    path('', views.about_me, name='about'),
]
