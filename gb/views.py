from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
from .forms import PostForm


def view_post(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'view_post.html', {
        'the_post': post
    })


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponse(post.content)
    else:
        form = PostForm()

    return render(request, 'new_post.html', {
        'form': form
    })
