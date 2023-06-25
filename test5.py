import csv
import requests

apiurl = "http://api.vworld.kr/req/address?"

ssg_list = []
with open('C:/Users/zptmz/OneDrive/바탕 화면/전월세,실거래가정보/서울시부동산전월세가25.csv', 'r') as r:
    data_list = csv.reader(r)
    next(data_list)
    # count = 0

    for data in data_list:
        ssg_list.append(data[2] + ' ' + data[4] + ' ' + data[7].lstrip('0') + ' ' + data[8].lstrip('0'))

ssg_list2 = []

c1 = 0

for item in ssg_list:
    params = {
        "service": "address",
        "request": "getcoord",
        "crs": "epsg:4326",
        "address": item,
        "format": "json",
        "type": "parcel",
        "key": "7F333705-8E22-391D-A774-644985B13EDD"
    }

    response = requests.get(apiurl, params=params, timeout=1200)
    if response.status_code == 200:
        # print(f'{response.json()}\n')

        input1 = response.json().get('response', {}).get('input')
        if input1:
            address = input1.get('address')
            if address:
                ssg_list2.append(address)

        result = response.json().get('response', {}).get('result')
        if result:
            point = result.get('point')
            if point:
                ssg_list2.append(point)

with open('C:/Users/zptmz/OneDrive/바탕 화면/전월세,실거래가정보/서울시부동산전월세가25(위도,경도).csv', 'w', newline='') as w:
    write = csv.writer(w)

    for i in range(0, len(ssg_list2), 2):
        address = ssg_list2[i]
        x = ssg_list2[i + 1]['x']
        y = ssg_list2[i + 1]['y']

        write.writerows([[address, x, y]])

    print('쓰기 성공')

# print(ssg_list2)