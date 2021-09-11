from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.core.paginator import Paginator

from .models import Article
from .forms import ArticleForm


@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')

    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')  # url 뒤에 붙이는 번호
    page_obj = paginator.get_page(page_number)

    context = {
        # 'articles': articles,
        'page_obj': page_obj,
    }
    return render(request, 'articles/index.html', context)


@require_safe
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
        'name': 'CREATE',
    }
    return render(request, 'articles/form.html', context)


@require_http_methods(['POST', 'GET'])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'name': 'UPDATE',
    }
    return render(request, 'articles/form.html', context)


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')