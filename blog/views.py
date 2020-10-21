from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Binod',
        'title': 'Blog post 1',
        'content': 'First Post Content',
        'date_posted': 'August 28, 2020'
    },
    {
        'author': 'Sandhya',
        'title': 'Blog post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 29, 2020'
    }
]


def home(request):
    # return HttpResponse('<h1> This is blog page</h1>')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
