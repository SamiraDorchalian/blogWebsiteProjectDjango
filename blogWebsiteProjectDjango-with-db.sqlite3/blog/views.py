from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post

def post_list_view(reuest):
    posts_list = Post.objects.filter(status='pub')
    return render(reuest, 'blog/posts_list.html', {'posts_list': posts_list})

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
