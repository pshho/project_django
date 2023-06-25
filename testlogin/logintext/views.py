from django.shortcuts import render, redirect

from .forms import ProfileForm


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # 프로필 목록 페이지로 리디렉션
    else:
        form = ProfileForm()
    return render(request, 'account/singup.html', {'form': form})
