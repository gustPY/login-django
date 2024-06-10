# GBlogin/urls.py

from django.contrib import admin
from django.urls import path
from django.urls import include

from homepage.views import homepage  # Import the homepage view

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    # Include the homepage view for the root URL
    path('', homepage, name='homepage'),
]
