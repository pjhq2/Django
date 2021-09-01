from django.shortcuts import render
from .models import Article


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    created_at = request.POST.get('created_at')
    updated_at = request.POST.get('updated_at')

    article = Article(title=title, content=content, created_at=created_at, updated_at=updated_at)
    article.save()

    return render(request, 'articles/create.html')


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)