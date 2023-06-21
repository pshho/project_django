import csv
import json
import urllib

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from poll.models import Question

def index(request):
    return render(request, 'poll/index.html')

def poll_list(request):
    question_list = Question.objects.all()
    # return HttpResponse("<h1>Welcome, Django</h1><br><h2>앞으로 잘 부탁해</h2>")
    return render(request, 'poll/poll_list.html', {'question_list':question_list})

def test(request):
    cart = "콩나물"  # 모델(데이터) - dictionary 형으로 전달
    cartlist = ["계란", "콩나물", "생수"]
    context = {'cart': cart, 'cartlist': cartlist}
    return render(request, 'poll/test.html', context)

def detail(request, question_id):
    # 데이터 1개 조회
    question = Question.objects.get(id=question_id)
    return render(request, 'poll/detail.html', {'question':question})

def vote(request, question_id):
    question = Question.objects.get(id=question_id)

    if request.method == "POST":
        try:
            choice_id = request.POST['choice']                  # 선택된 항목 id
            sel_choice = question.choice_set.get(id=choice_id)  # id로 항목을 찾아서

        except:
            error = "선택을 하지 않았습니다."

            return render(request, 'poll/detail.html', {"question":question, "error":error})

        else:
            sel_choice.votes += 1                               # choice relation의 votes에 1 더하기
            sel_choice.save()                                   # 저장 필수

    else:
        return render(request, 'poll/detail.html', {'question': question})

    return render(request, 'poll/result.html', {'question': question})

def search(request):
    if request.method == 'GET':

        context = {}

        client_id = "Gr3DZKpSitjNw83linRK"
        client_secret = "CM1z5bCrQ6"
        q = request.GET.get('q')
        encText = urllib.parse.quote('{}'.format(q))
        sort = 'random'
        display = 5

        url = f"https://openapi.naver.com/v1/search/local.json?query={encText}&display={display}&sort={sort}"
        req = urllib.request.Request(url)
        req.add_header("X-Naver-Client-Id", client_id)
        req.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(req)
        rescode = response.getcode()

        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            sub_items = []

            for item in items:
                sub_item = {
                    'title':item.get('title'),
                    'category': item.get('category'),
                    'address':item.get('address'),
                    'roadAddress':item.get('roadAddress')
                }

                sub_items.append(sub_item)

            context = {
                'items':sub_items
            }

        else:
            print("Error Code:" + rescode)

        return JsonResponse(context)

def search2(request):
    return render(request, 'poll/search.html')

def mapmarket(request):
    if request.method == 'GET':

        client_id = "Gr3DZKpSitjNw83linRK"
        client_secret = "CM1z5bCrQ6"
        q = request.GET.get('q')
        encText = urllib.parse.quote('{}'.format(q))
        sort = 'random'
        display = 5

        url = f"https://openapi.naver.com/v1/search/local.json?query={encText}&display={display}&sort={sort}"
        req = urllib.request.Request(url)
        req.add_header("X-Naver-Client-Id", client_id)
        req.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(req)
        rescode = response.getcode()

        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            sub_items = []

            for item in items:
                sub_item = {
                    'title':item.get('title'),
                    'category': item.get('category'),
                    'address':item.get('address'),
                    'roadAddress':item.get('roadAddress')
                }

                sub_items.append(sub_item)

            context = {
                'items':sub_items
            }

        else:
            print("Error Code:" + rescode)

        return JsonResponse(context)




    with open('./polls/static/poll/resources/서울시부동산정보.csv', 'r') as r:
        data_list = csv.reader(r)
        ssg_list = []
        count = 0
        for data in data_list:
            if data[7] != '' or data[8] != '' or data[15] != '':
                if data[8] != '0000':
                    result = data[2] + ' ' + data[4] + ' ' + data[7] + ' ' + data[8]
                    ssg_list.append(result)
                    count += 1
                elif data[8] == '0000':
                    result = data[2] + ' ' + data[4] + ' ' + data[7]
                    ssg_list.append(result)
                    count += 1

    print(ssg_list)
    print(count)

    context = {
        'ssg_list':ssg_list
    }
    return JsonResponse(context)
