from django.shortcuts import render, redirect

from blog.forms import PostForm
from blog.models import Post
from django.utils import timezone


def index(request):
    return render(request, 'blog/index.html')

def post_list(request):
    post_list = Post.objects.all()
    context = {'post_list':post_list}
    return render(request, 'blog/post_list.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post':post}
    return render(request, 'blog/detail.html', context)

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)    # (데이터, 파일 같이 가져오기)

        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()

            return redirect('blog:post_list')
    else:
        form = PostForm()

    context = {'form':form}
    return render(request, 'blog/post_form.html', context)