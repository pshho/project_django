from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

from common.forms import UserForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = AuthenticationForm(username=username, password=password)

            login(request, user)    # 자동 로그인

            return redirect('/')
    else:
        form = UserForm()

    context = {
        'form':form
    }

    return render(request, 'common/signup.html', context)
