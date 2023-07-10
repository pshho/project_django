from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import PostForm, CommentForm
from .models import Post, Category, Comment
from django.utils import timezone

def index(request):
    # 최신글 3개 보내기
    new_post = Post.objects.order_by('-pub_date')[0:3]
    context = {
        'new_post': new_post,
    }
    return render(request, 'blog/index2.html', context)

def post_list(request):
    post_list = Post.objects.order_by('-pub_date')
    categories = Category.objects.all()
    total = Post.objects.count()

    kw = request.GET.get('kw', '')

    if kw:
        post_list = post_list.filter(
            Q(title__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(author__username__icontains=kw)  # 글쓴이 검색
        ).distinct()

    context = {'post_list':post_list, 'categories':categories, 'kw': kw, 'total': total}
    return render(request, 'blog/post_list.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    categories = Category.objects.all()
    context = {'post':post, 'categories':categories}
    return render(request, 'blog/detail.html', context)

@login_required(login_url='common:login')
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)    # (데이터, 파일 같이 가져오기)

        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.author = request.user
            post.save()

            return redirect('blog:post_list')
    else:
        form = PostForm()

    context = {'form':form}
    return render(request, 'blog/post_form.html', context)

# 카테고리 페이지 처리
def category_page(request, slug):
    current_category = Category.objects.get(slug=slug)
    post_list = Post.objects.filter(category=current_category)
    post_list = post_list.order_by('-pub_date')
    total = Post.objects.count()
    categories = Category.objects.all()

    context = {
        'current_category': current_category,
        'post_list': post_list,
        'categories': categories,
        'total': total,
    }

    return render(request, 'blog/post_list.html', context)

@login_required(login_url='common:login')
def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('blog:post_list')

@login_required(login_url='common:login')
def comment_create(request, post_id):
    # 댓글 쓰기 위한 외래키로 연결된 포스트
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        # 댓글 폼 연동
        form = CommentForm(request.POST)    # 입력된 댓글 가져오기

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.pub_date = timezone.now()
            comment.post = post
            form.save()

            return redirect('blog:detail', post_id=post_id)

    form = CommentForm()
    context = {'form': form}
    return redirect('blog:detail', context, post_id=post_id)

@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    return redirect('blog:detail', post_id=comment.post.id)

@login_required(login_url='common:login')
def comment_update(request, comment_id):
    comment = Comment.objects.get(id=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            form.save()

            return redirect('blog:detail', post_id=comment.post.id)

    context = {
        'comment': comment,
    }

    return render(request, 'blog/comment_form.html', context)