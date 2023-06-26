import csv
import json

import chardet as chardet

csv_file_path = 'static/poll/resources/seoul1.csv'
json_file_path = 'seoulestate2.json'
encoding = 'cp949'

data = []


def get_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

encoding = get_encoding(csv_file_path)
# print(encoding)


# CSV 파일 열기
with open(csv_file_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)

    # CSV 데이터 읽기
    for row in reader:
        model = 'poll.Seoulestate2'
        fields = row
        converted_item = {'model':model, 'fields':fields}
        data.append(converted_item)

# JSON 파일로 변환하여 저장
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)


