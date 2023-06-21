import csv
import requests
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

'''
with open('./polls/static/poll/resources/서울시부동산정보.csv', 'r') as r:
    data_list = csv.reader(r)
    ssg_list = []
    # count = 0
    for data in data_list:
        if data[7] != '' or data[8] != '' or data[15] != '':
            if data[8] != '0000':
                result = data[2] + ' ' + data[4] + ' ' + data[7] + ' ' + data[8]
                ssg_list.append(result)
                # count += 1
            elif data[8] == '0000':
                result = data[2] + ' ' + data[4] + ' ' + data[7]
                ssg_list.append(result)
                # count += 1
'''

with open('./polls/static/poll/resources/강남구.csv', 'r') as r:
    data_list = csv.reader(r)
    ssg_list = []
    # count = 0

    for item in data_list:
        if len(item) >= 4:
            result = item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[3]
            ssg_list.append(result)
            # count += 1
        else:
            result = item[0] + ' ' + item[1] + ' ' + item[2]
            ssg_list.append(result)
            # count += 1

url_front = "http://api.vworld.kr/req/address?"
url_params = "service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type=road"
url_address = "&address="
url_key = "&key="
auth_key = "7F333705-8E22-391D-A774-644985B13EDD"

count = 0
for addr in ssg_list:
    address = addr

    # url 완성
    url = url_front + url_params + url_address + address + url_key + auth_key

    result = requests.get(url)
    json_data = result.json()

    if json_data['response']['status'] == 'OK':
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        print("\n경도: ", x, "\n위도: ", y)
        count += 1

print(count)




# print(url)



# print(json_data)



# print(ssg_list)
# print(count)
