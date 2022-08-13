from django.urls import path
from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.get_entry, name="entry"),
    path("<str:title>/edit/", views.edit, name="edit"),
    path("search/", views.search, name="search"),
    path("new/", views.new, name="new"),
    path("random/", views.random, name="random")
]
