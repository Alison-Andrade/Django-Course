from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
        'autor': 'Alison',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 08, 2019'
    },
    {
        'autor': 'Fábio',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 09, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
