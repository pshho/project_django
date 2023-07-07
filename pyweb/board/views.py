from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from board.forms import QuestionForm, AnswerForm
from board.models import Question, Answer


def index(request):
    return render(request, 'board/index.html')

def question_list(request):
    question_list = Question.objects.order_by('-create_date')
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list':page_obj}

    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    # 모델에서 데이터가 있으면 가져오고 없으면 404페이지 오류 처리
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}

    return render(request, 'board/detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)

        if form.is_valid(): # 폼이 유효성 검사를 통과했다면
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            form.save()

            return redirect('board:question_list')
    else:
        form = QuestionForm()

    context = {'form':form}
    return render(request, 'board/question_form.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)    # content만 저장
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            form.save()

            return redirect('board:detail', question_id=question_id)

    else:
        form = AnswerForm()

    context = {'question':question, 'form':form}

    return render(request, 'board/detail.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    question.delete()

    return redirect('board:question_list')

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    # question = Question.objects.get(id=question_id)
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()

    return redirect('board:detail', question_id=answer.question.id)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.author = request.user
            question.save()

            return redirect('board:detail', question_id=question_id)

    else:
        form = QuestionForm(instance=question)

    context = {'form':form}

    return render(request, 'board/question_form.html', context)