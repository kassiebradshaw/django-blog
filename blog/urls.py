from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.blog_list, name="blog-list"),
    # path("/posts/my-first-post")
]