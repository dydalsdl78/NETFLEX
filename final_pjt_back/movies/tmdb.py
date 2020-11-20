import requests
import json

api_key = "d7a0f6399832ff632e1b02fc2afb5d21"

data = []

for page in range(0, 10):
    url = "https://api.themoviedb.org/3/movie/popular?api_key=" + api_key + "&language=ko-KR&page=" + str(page + 1)
    # 응답
    response = requests.get(url)
    # 응답값 저장
    tmp = json.loads(response.text)

    # 한번에 20개의 데이터를 반복문을 돌면서
    for i in range(20):
        tmp['results'][i].pop('id')
        # 한개의 딕셔너리 안에 "model" : "movies.movie" 라는 키, 값 형태로 저장
        data.append({"model": "movies.movie"})
        # 전체 필드를 "fields": tmp[results][i] 키, 값 형태로 저장
        data[20 * page + i]["fields"] = tmp['results'][i]


file_path = "./fixtures/movies.json"

with open(file_path, 'w', encoding='UTF-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)