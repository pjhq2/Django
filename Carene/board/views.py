from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.contrib.auth import get_user

from .models import Board
from .forms import BoardForm


@require_safe
def index(request):
    board = Board.objects.order_by('-pk')
    paginator = Paginator(board, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'board/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    user = get_user(request)
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('board:detail', post.pk)
    else:
        form = BoardForm()
    context = {
        'form': form,
    }
    return render(request, 'board/form.html', context)


@require_safe
def detail(request, post_pk):
    post = get_object_or_404(Board, pk=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'board/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, post_pk):
    post = get_object_or_404(Board, pk=post_pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('board:detail', post.pk)
    else:
        form = BoardForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, 'board/form.html', context)


@require_POST
def delete(request, post_pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Board, pk=post_pk)
        post.delete()
    return redirect('board:index')
