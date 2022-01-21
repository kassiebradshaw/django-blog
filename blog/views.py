from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.

blog_posts = {
    "My First Post": "Here it is, my very first post!",
    "My Second Post": "Well I've done it again, I've made a second blog post.",
    "My Third Post": "Once more, I have posted. Huzzah",
}

# View that displays the blog landing page listing latest blog posts and some welcome text
def index(request):

    return render(request, "blog/index.html")

# View that lists all the blog posts
def blog_list(request):
    posts = list(blog_posts.keys())

    return render(request, "blog/blog_list.html", {
        "posts": posts,
    })

# View that loads full blog post
def view_blog_post(request, post):
    pass
