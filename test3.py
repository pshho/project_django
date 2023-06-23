from datetime import datetime, timedelta

import requests

now = datetime.now()
now_year = now.year
now_month = now.month
next_month = now + timedelta(days=30)
month = now.strftime('%m')
month2 = next_month.strftime('%m')

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
result1 = requests.get(reqUrl1)
json_data1 = result1.json()

# count = 0
# 주택관리번호 추출
house_manage = 0

data_list = []
# APT 분양정보 청약 접수 시작일
for data in json_data1['data']:
    if '부천역 청담더마크' == data['HOUSE_NM']:
        if f'{now_year}-{month}' in data['RCEPT_BGNDE']:
            house_manage = data['HOUSE_MANAGE_NO']
            data_list.append(data)
        elif f'{now_year}-{month2}' in data['RCEPT_BGNDE']:
            house_manage = data['HOUSE_MANAGE_NO']
            data_list.append(data)
            # count += 1
            # print(data)

# 오피스텔/도시형/민간임대 분양정보 청약 접수 시작일
result2 = requests.get(reqUrl2)
json_data2 = result2.json()

for data in json_data2['data']:
    if '부천역 청담더마크' == data['HOUSE_NM']:
        if f'{now_year}-{month}' in data['SUBSCRPT_RCEPT_BGNDE']:
            house_manage = data['HOUSE_MANAGE_NO']
            data_list.append(data)
        elif f'{now_year}-{month2}' in data['SUBSCRPT_RCEPT_BGNDE']:
            house_manage = data['HOUSE_MANAGE_NO']
            data_list.append(data)
            # count += 1
            # print(data)

# APT 무순위/잔여세대 일반 공급 접수 시작일
result3 = requests.get(reqUrl3)
json_data3 = result3.json()

for data in json_data3['data']:
    if '부천역 청담더마크' == data['HOUSE_NM']:
        if f'{now_year}-{month}' in data['SUBSCRPT_RCEPT_BGNDE']:
            house_manage = data['HOUSE_MANAGE_NO']
            data_list.append(data)
        elif f'{now_year}-{month2}' in data['SUBSCRPT_RCEPT_BGNDE']:
            house_manage = data['HOUSE_MANAGE_NO']
            data_list.append(data)

result4 = requests.get(reqUrl4)
json_data4 = result4.json()
for data in json_data4['data']:
    if house_manage == data['HOUSE_MANAGE_NO']:
        data_list.append(data)

result5 = requests.get(reqUrl5)
json_data5 = result5.json()
for data in json_data5['data']:
    if house_manage == data['HOUSE_MANAGE_NO']:
        data_list.append(data)

result6 = requests.get(reqUrl6)
json_data6 = result6.json()
for data in json_data6['data']:
    if house_manage == data['HOUSE_MANAGE_NO']:
        data_list.append(data)

print(house_manage)
print(data_list)