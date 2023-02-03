from django.shortcuts import render, get_object_or_404
from .models import Post, Group


ITEMS_PER_PAGE: int = 10


# The main page.
def index(request):
    template = "posts/index.html"
    title = "Последние обновления на сайте."
    posts = Post.objects.select_related("author", "group")[:ITEMS_PER_PAGE]

    context = {"posts": posts, "title": title}
    return render(request, template, context)


# The group posts page.
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    template = "posts/group_list.html"
    posts = group.posts.select_related("author")[:ITEMS_PER_PAGE]
    context = {
        "group": group,
        "posts": posts,
    }
    return render(request, template, context)
