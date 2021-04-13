from django.shortcuts import render
from .models import Blogpost
from django.http import HttpResponse


# Create your views here.

def index(request):
    allPosts = Blogpost.objects.all()
    posts = []
    for post in allPosts:
        posts.append(post)
    params = {'posts': posts}
    print(params)
    return render(request, 'blog/index.html', params)


def blogpost(request, id):
    post = Blogpost.objects.filter(blog_id=id)[0]
    return render(request, 'blog/blogpost.html', {'post': post})
