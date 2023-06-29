import csv
import json
import os
import urllib
import requests
import logging
import asyncio
import aiohttp

from datetime import datetime, timedelta

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers

from .models import Question, SeouljRent, SeoulReal

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

# 지도 표시 html 보냄
def search(request):
    return render(request, 'poll/search.html')

# 지도 검색 함수
def search2(request):
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
                    'title': item.get('title'),
                    'category': item.get('category'),
                    'address': item.get('address'),
                    'roadAddress': item.get('roadAddress')
                }
                sub_items.append(sub_item)
            context = {
                'items': sub_items,
            }
        else:
            print("Error Code:" + rescode)

        return JsonResponse(context)
    return JsonResponse({'result': '실패'})

def map_convert(request):
    if request.method == 'GET':
        seoul_rent = SeouljRent.objects.all()
        seoul_real = SeoulReal.objects.all()
        jrent = [model_to_dict(seoul) for seoul in seoul_rent]
        real = [model_to_dict(seoul) for seoul in seoul_real]

        results = {
            'jrent':jrent,
            'real':real
        }
        return JsonResponse(results, safe=False)

    return JsonResponse({'result': '실패'})

# 이전 달, 현재 연도 당월, 다음달
now = datetime.now()
now_year = now.year
now_month = now.month
next_month = now + timedelta(days=30)

# 이전 달 계산
if now_month == 1:
    previous_month = 12
    previous_year = now_year - 1
else:
    previous_month = now_month - 1
    previous_year = now_year
month = now.strftime('%m')
month2 = next_month.strftime('%m')
previous_month_str = str(previous_month).zfill(2)  # 한 자리 숫자일 경우 0을 추가하여 두 자리로 맞춤

# 비동기 처리 함수
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# calendar에 청약 일정 추가하는 함수
async def calendar(request):
    if request.method == 'GET':

        url1 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail?'
        page = 'page=1&'
        perPage = 'perPage=10000&'
        serviceKey = 'serviceKey=ibEJT6J0bl9WzpzbwJVPg9on2aBStbXKZnT8a7sLOTuEi5LMGvjsPAufQYld%2Br%2FvL6B4VhxXZ5EnI7j1GO%2B8uQ%3D%3D'

        url2 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getUrbtyOfctlLttotPblancDetail?'
        url3 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getRemndrLttotPblancDetail?'

        reqUrl1 = url1 + page + perPage + serviceKey
        reqUrl2 = url2 + page + perPage + serviceKey
        reqUrl3 = url3 + page + perPage + serviceKey

        tasks = [
            fetch_data(reqUrl1),
            fetch_data(reqUrl2),
            fetch_data(reqUrl3)
        ]

        # 비동기로 모든 작업 실행
        responses = await asyncio.gather(*tasks)

        json_data1, json_data2, json_data3 = responses

        data_list = []
        # APT 분양정보 청약 접수 시작일
        for data in json_data1['data']:
            if f'{now_year}-{month}' in data['RCEPT_BGNDE']:
                data_list.append(data)
            elif f'{now_year}-{month2}' in data['RCEPT_BGNDE']:
                data_list.append(data)
            elif f'{previous_year}-{previous_month_str}' in data['RCEPT_BGNDE']:
                data_list.append(data)

        # 오피스텔/도시형/민간임대 분양정보 청약 접수 시작일
        for data in json_data2['data']:
            if f'{now_year}-{month}' in data['SUBSCRPT_RCEPT_BGNDE']:
                data_list.append(data)
            elif f'{now_year}-{month2}' in data['SUBSCRPT_RCEPT_BGNDE']:
                data_list.append(data)
            elif f'{previous_year}-{previous_month_str}' in data['SUBSCRPT_RCEPT_BGNDE']:
                data_list.append(data)

        # APT 무순위/잔여세대 일반 공급 접수 시작일
        for data in json_data3['data']:
            if f'{now_year}-{month}' in data['SUBSCRPT_RCEPT_BGNDE']:
                data_list.append(data)
            elif f'{now_year}-{month2}' in data['SUBSCRPT_RCEPT_BGNDE']:
                data_list.append(data)
            elif f'{previous_year}-{previous_month_str}' in data['SUBSCRPT_RCEPT_BGNDE']:
                data_list.append(data)

        results = []

        for data in data_list:
            if 'RCEPT_BGNDE' in data:
                result = {
                    'title': data['HOUSE_NM'],
                    'start': data['RCEPT_BGNDE']
                }
                results.append(result)
            elif 'SUBSCRPT_RCEPT_BGNDE' in data:
                result = {
                    'title': data['HOUSE_NM'],
                    'start': data['SUBSCRPT_RCEPT_BGNDE']
                }
                results.append(result)

        context = {
            'context':results
        }
        return render(request, 'poll/calendar.html', context)

    return render(request, 'poll/calendar.html')

# 달력 iframe 출력
async def calendar_iframe(request, title):
    if request.method == 'GET':

        url1 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail?'
        page = 'page=1&'
        perPage = 'perPage=10000&'
        serviceKey = 'serviceKey=ibEJT6J0bl9WzpzbwJVPg9on2aBStbXKZnT8a7sLOTuEi5LMGvjsPAufQYld%2Br%2FvL6B4VhxXZ5EnI7j1GO%2B8uQ%3D%3D'

        url2 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getUrbtyOfctlLttotPblancDetail?'
        url3 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getRemndrLttotPblancDetail?'
        url4 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancMdl?'
        url5 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getUrbtyOfctlLttotPblancMdl?'
        url6 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getRemndrLttotPblancMdl?'

        reqUrl1 = url1 + page + perPage + serviceKey
        reqUrl2 = url2 + page + perPage + serviceKey
        reqUrl3 = url3 + page + perPage + serviceKey
        reqUrl4 = url4 + page + perPage + serviceKey
        reqUrl5 = url5 + page + perPage + serviceKey
        reqUrl6 = url6 + page + perPage + serviceKey

        tasks = [
            fetch_data(reqUrl1),
            fetch_data(reqUrl2),
            fetch_data(reqUrl3),
            fetch_data(reqUrl4),
            fetch_data(reqUrl5),
            fetch_data(reqUrl6),
        ]

        # 비동기로 모든 작업 실행
        responses = await asyncio.gather(*tasks)

        json_data1, json_data2, json_data3, json_data4, json_data5, json_data6 = responses

        # 주택관리번호 추출
        house_manage = 0
        data_list = []
        data_list2 = []

        # APT 분양정보 청약 접수 시작일
        for data in json_data1['data']:
            if title == data['HOUSE_NM']:
                if f'{now_year}-{month}' in data['RCEPT_BGNDE']:
                    house_manage = data['HOUSE_MANAGE_NO']
                    data_list.append(data)
                elif f'{now_year}-{month2}' in data['RCEPT_BGNDE']:
                    house_manage = data['HOUSE_MANAGE_NO']
                    data_list.append(data)
                elif f'{previous_year}-{previous_month_str}' in data['RCEPT_BGNDE']:
                    house_manage = data['HOUSE_MANAGE_NO']
                    data_list.append(data)

        for data in json_data2['data']:
            if title == data['HOUSE_NM']:
                if f'{now_year}-{month}' in data['SUBSCRPT_RCEPT_BGNDE']:
                    house_manage = data['HOUSE_MANAGE_NO']
                    data_list.append(data)
                elif f'{now_year}-{month2}' in data['SUBSCRPT_RCEPT_BGNDE']:
                    house_manage = data['HOUSE_MANAGE_NO']
                    data_list.append(data)
                elif f'{previous_year}-{previous_month_str}' in data['SUBSCRPT_RCEPT_BGNDE']:
                    house_manage = data['HOUSE_MANAGE_NO']
                    data_list.append(data)

        for data in json_data3['data']:
            if title == data['HOUSE_NM']:
                if f'{now_year}-{month}' in data['SUBSCRPT_RCEPT_BGNDE']:
                    house_manage = data['HOUSE_MANAGE_NO']
                    data_list.append(data)
                elif f'{now_year}-{month2}' in data['SUBSCRPT_RCEPT_BGNDE']:
                    house_manage = data['HOUSE_MANAGE_NO']
                    data_list.append(data)
                elif f'{previous_year}-{previous_month_str}' in data['SUBSCRPT_RCEPT_BGNDE']:
                    house_manage = data['HOUSE_MANAGE_NO']
                    data_list.append(data)

        for data in json_data4['data']:
            if house_manage == data['HOUSE_MANAGE_NO']:
                data_list2.append(data)

        for data in json_data5['data']:
            if house_manage == data['HOUSE_MANAGE_NO']:
                data_list2.append(data)

        for data in json_data6['data']:
            if house_manage == data['HOUSE_MANAGE_NO']:
                data_list2.append(data)

        rowspan = len(data_list2) + 1

        context = {
            'data_list':data_list,
            'data_list2':data_list2,
            'rowspan':rowspan
        }

        return render(request, 'poll/calendar_iframe.html', context)

    return render(request, 'poll/calendar_iframe.html')
