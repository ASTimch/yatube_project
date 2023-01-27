from django.shortcuts import render
from django.http import HttpResponse

# The main page.
def index(request):
    return HttpResponse("You're at the posts index.")


# The group posts page.
def group_posts(request, slug):
    return HttpResponse(f"You're at the group <b>{slug}</b> posts.")
