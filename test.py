import csv
import urllib.request
import json

'''
url = 'http://openapi.seoul.go.kr:8088/4d6e42445a746d6437354e65737162/json/tbLnOpendataRentV/1/1000/'

response = urllib.request.urlopen(url)
response_message = response.read().decode('utf8')

data = json.loads(response_message)
# total_count = data['tbLnOpendataRentV']['list_total_count']

sgg_names = []  # 서울시 구단위를 저장할 빈배열
count = 0

for item in data['tbLnOpendataRentV']['row']:
    # 리스트 중에 구단위 전부 저장(중복도 되게)
    sgg_nm = item['BLDG_NM']

    # 없으면 넣어라 조건문
    if sgg_nm not in sgg_names:
        # 없으면 넣기때문에 중복을 걸러줌
        sgg_names.append(sgg_nm)
        count += 1

print(count)

    # 혹시 강남구면

# 구단위 출력
# for sgg_name in sgg_names:
#     print(sgg_name)

'''
with open('./polls/static/poll/resources/서울시부동산정보.csv', 'r') as r:
    data_list = csv.reader(r)
    ssg_list = []
    for data in data_list:
        ssg_list.append(data[0])

print(ssg_list)
