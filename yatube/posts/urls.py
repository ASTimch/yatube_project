# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # main page
    path('', views.index),
    # groups page
    path('group/<slug:slug>/', views.group_posts),
]
