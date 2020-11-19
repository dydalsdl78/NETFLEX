import requests
import json

api_key = "d7a0f6399832ff632e1b02fc2afb5d21"

data = []

for page in range(1, 11):
    url = "https://api.themoviedb.org/3/movie/popular?api_key=" + api_key + "&language=ko-KR&page=" + str(page)

    response = requests.get(url)

    tmp = json.loads(response.text)

    data.extend(tmp['results'])

file_path = "./movies.json"

with open(file_path, 'w', encoding='UTF-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)