import requests
import json

api_key = "d7a0f6399832ff632e1b02fc2afb5d21"

data = []
pages = 10

for page in range(0, pages):
    url = "https://api.themoviedb.org/3/movie/popular?api_key=" + \
        api_key + "&language=ko-KR&page=" + str(page + 1)
    # 응답
    response = requests.get(url)
    # 응답값 저장
    tmp = json.loads(response.text)
    # 한번에 20개의 데이터를 반복문을 돌면서
    for i in range(20):
        tmp['results'][i].pop('id')
        tmp['results'][i]['id'] = i
        tmp['results'][i]['name'] = tmp['results'][i]['title']

        data.append({"id": i, "name": tmp['results'][i]['title']})

    print(data)

file_path = "./movies.json"

with open(file_path, 'w', encoding='UTF-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)
