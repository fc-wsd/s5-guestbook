from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def hello(request, pk, hello):
    print(hello)
    msg = 'Kay'
    return render(
        request,
        'hello.html',
        {'message': msg}
    )

