from django.urls import path
from . import views

# URL pattern for the contact page
urlpatterns = [
    path('', views.contact_me, name='contact'),
]
