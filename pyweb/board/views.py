from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from board.forms import QuestionForm, AnswerForm
from board.models import Question

def index(request):
    return render(request, 'board/index.html')

def question_list(request):
    question_list = Question.objects.all()
    context = {'question_list':question_list}
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question':question}
    return render(request, 'board/detail.html', context)

def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)

        if form.is_valid(): # 폼이 유효성 검사를 통과했다면
            question = form.save(commit=False)
            question.create_date = timezone.now()
            form.save()

            return redirect('board:question_list')
    else:
        form = QuestionForm()

    context = {'form':form}
    return render(request, 'board/question_form.html', context)

def answer_create(request, question_id):
    question = Question.objects.get(id=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)    # content만 저장
            answer.create_date = timezone.now()
            answer.question = question
            form.save()

            return redirect('board:detail', question_id=question_id)

    else:
        form = AnswerForm()

    context = {'question':question, 'form':form}



    return render(request, 'board/detail.html', context)