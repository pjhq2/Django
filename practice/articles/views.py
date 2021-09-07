from django.shortcuts import render, redirect
from .models import Article

# CREATE
def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    created_at = request.POST.get('created_at')
    updated_at = request.POST.get('updated_at')
    if len(title) > 0 and len(content) > 0:
        article = Article(title=title, content=content, created_at=created_at, updated_at=updated_at)
        article.save()
        return render(request, 'articles/create.html')
    else:
        return redirect('articles:new')


# READ
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# UPDATE
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.updated_at = request.POST.get('updated_at')
    if len(article.title) > 0 and len(article.content) > 0:
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        return redirect('articles:edit', article.pk)


# DELETE
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST' or request.method == 'GET':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)