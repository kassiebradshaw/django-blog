from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from datetime import date

# Create your views here.

blog_posts = [
    {
        "slug": "my-first-post",
        "image": "animalcrossing.jpg",
        "author": "Kassie",
        "date": date(2022, 1, 31),
        "title": "My First Post",
        "excerpt": "Here it is, my very first post!",
        "content": """
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.
        """,
    },

    {
        "slug": "my-second-post",
        "image": "stardewvalley.jpg",
        "author": "Kassie",
        "date": date(2022, 1, 31),
        "title": "My Second Post",
        "excerpt": "Well I've done it again, I've made a second blog post.",
        "content": """
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.
        """,

    },

    {
        "slug": "my-third-post",
        "image": "minecraft.jpg",
        "author": "Kassie",
        "date": date(2022, 1, 31),
        "title": "My Third Post",
        "excerpt": "Once more, I have posted. Huzzah!",
        "content": """
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.
        """,
    },

    {
        "slug": "my-fourth-post",
        "image": "colorful.jpg",
        "author": "Kassie",
        "date": date(2022, 1, 31),
        "title": "My Fourth Post",
        "excerpt": "The rainbow is my favorite color! What's yours?",
        "content": """
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.
        """,
    },

    {
        "slug": "my-fifth-post",
        "image": "crochet.jpg",
        "author": "Kassie",
        "date": date(2022, 1, 31),
        "title": "My Fifth Post",
        "excerpt": "I sure do like to crochet...",
        "content": """
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.
        """,
    },

    {
        "slug": "my-sixth-post",
        "image": "hufflepuff.jpg",
        "author": "Kassie",
        "date": date(2022, 1, 31),
        "title": "My Sixth Post",
        "excerpt": "Hufflepuff is THE best",
        "content": """
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.
        """,
    },

    {
        "slug": "my-seventh-post",
        "image": "supernatural.png",
        "author": "Kassie",
        "date": date(2022, 1, 31),
        "title": "My Seventh Post",
        "excerpt": "This one has a picture from Supernatural",
        "content": """
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.

        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam, quae, quia debitis corrupti illo totam inventore aliquam maiores dolorum perspiciatis aspernatur aliquid quidem impedit hic eius, ipsa natus. Autem, explicabo.
        """,
    },
]

def get_date(post):
    return post.get('date') #or can use post['date']

# View that displays the blog landing page listing latest blog posts and some welcome text
def starting_page(request):
    sorted_posts = sorted(blog_posts, key=get_date)
    latest_posts = sorted_posts[-3:]

    return render(request, "blog/starting_page.html", {
        "posts": latest_posts,
    })

# View that lists all the blog posts
def posts(request):
    posts = list(blog_posts.keys())

    return render(request, "blog/all_posts.html", {
        "posts": posts,
    })

# View that loads full blog post
def post_detail(request, slug):
    return render(request, "blog/post_detail.html")
