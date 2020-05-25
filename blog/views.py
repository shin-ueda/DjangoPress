from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category, Tag


def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/post_list.html', {
                                                'posts': posts,
                                                'categories': categories,
                                                'tags': tags})
