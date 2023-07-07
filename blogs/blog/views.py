from django.db.models import Q
from django.shortcuts import render, redirect

from blog.forms import PostForm
from blog.models import Post, Category
from django.utils import timezone

def index(request):
    # 최신글 3개 보내기
    new_post = Post.objects.order_by('-pub_date')[0:3]
    context = {
        'new_post': new_post,
    }
    return render(request, 'blog/index.html', context)

def post_list(request):
    post_list = Post.objects.all()
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

def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('blog:post_list')