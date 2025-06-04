from django.shortcuts import render

from .models import Post

def post_list_view(reuest):
    posts_list = Post.objects.all()
    return render(reuest, 'blog/posts_list.html', {'posts_list': posts_list})

