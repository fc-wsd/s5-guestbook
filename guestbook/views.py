from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse('hello world')
    print(request.user.is_authenticated())
    msg = 'Kay'
    return render(
        request,
        'hello.html',
        {'message': msg}
    )

