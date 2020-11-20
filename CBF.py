import pandas as pd
import numpy as np
import json
import warnings; warnings.filterwarnings('ignore')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer

# 데이터 불러오기
movies = pd.read_json("CBFmovies.json")

# 사용 할 데이터만 저장 
movies_df = movies[['id','title','overview','popularity','vote_count','vote_average','release_date','poster_path','adult','genre_ids']]


# 1.장르기반 ------------------------------------------------------------

# print(movies_df['genre_ids'])
movies_df['genre_ids'] = movies_df['genre_ids'].apply(lambda x : list(map(str, x)))
# print(type(movies_df['genre_ids'][0]))

# for x in range(len(movies_df)):
#     movies_df['genres_literal'] = list(map(str, x))

movies_df['genres_literal'] = movies_df['genre_ids'].apply(lambda x : (' ').join(x))

# CountVectorizer로 학습시켰더니 4803개 영화에 대한 276개 장르의 '장르 매트릭스'가 생성되었다.
count_vect = CountVectorizer(min_df=0, ngram_range=(1,2)) #min_df: 단어장에 들어갈 최소빈도, ngram_range: 1 <= n <= 2
genre_mat = count_vect.fit_transform(movies_df['genres_literal'])
print(genre_mat.shape)


# 코사인 유사도에 의해 4803개 영화 각각 유사한 영화들이 계산됨
from sklearn.metrics.pairwise import cosine_similarity
genre_sim = cosine_similarity(genre_mat, genre_mat)
print(genre_sim.shape)
print(genre_sim[:5])

# 자료를 정렬하는 것이 아니라 순서만 알고 싶다면 argsort
# 유사도가 높은 영화를 앞에서부터 순서대로 보여줌
# 0번째 영화의 경우 유사도 순서 : 0번, 3494번, 813번, ..., 2401 순서
genre_sim_sorted_ind = genre_sim.argsort()[:, ::-1] # 전체를 -1칸 간격으로
print(genre_sim_sorted_ind[:1])

from sklearn.metrics.pairwise import cosine_similarity
genre_sim = cosine_similarity(genre_mat, genre_mat)

# 가중 평점
# 상위 60%에 해당하는 vote_count를 최소 투표 횟수인 m으로 지정
C = movies_df['vote_average'].mean()
m = movies_df['vote_count'].quantile(0.6)

# 가중 평점 계산
def weighted_vote_average(record):
    v = record['vote_count']
    R = record['vote_average']
    
    return ( (v/(v+m)) * R ) + ( (m/(m+v)) * C )

# 기존 데이터에 가중평점 칼럼 추가
movies_df['weighted_vote'] = movies_df.apply(weighted_vote_average, axis=1)

def find_sim_movie_ver2(df, sorted_ind, title_name, top_n=10):
    title_movie = df[df['title'] == title_name]
    title_index = title_movie.index.values
    
    # top_n의 2배에 해당하는 쟝르 유사성이 높은 index 추출
    similar_indexes = sorted_ind[title_index, :(top_n*2)]
    similar_indexes = similar_indexes.reshape(-1)

    # 기준 영화 index는 제외
    similar_indexes = similar_indexes[similar_indexes != title_index]
    
    # top_n의 2배에 해당하는 후보군에서 weighted_vote 높은 순으로 top_n 만큼 추출 
    return df.iloc[similar_indexes].sort_values('weighted_vote', ascending=False)[:top_n]

similar_movies = find_sim_movie_ver2(movies_df, genre_sim_sorted_ind, '기생충',10)
print(similar_movies[['title', 'vote_average', 'weighted_vote', 'genre_ids', 'vote_count']])

# ---------------------------------------------------------------------

# 2.줄거리기반


# 줄거리가 없는 영화 제거
# idx = movies_df[movies_df['overview'] == ""].index
# new_movies_df = movies_df.drop(idx)

# print(new_movies_df)

# 불용어 설정
# tfidf = TfidfVectorizer(stop_words='english')
# # overview에 대해서 tf-idf 수행
# tfidf_matrix = tfidf.fit_transform(movies_df['overview'])


# # 코사인 유사도 계산
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# indices = pd.Series(movies_df.index, index=movies_df['title']).drop_duplicates()


# # def get_recommendations(title, cosine_sim=cosine_sim):
# #     # 선택한 영화의 타이틀로부터 해당되는 인덱스를 받아옵니다. 이제 선택한 영화를 가지고 연산할 수 있습니다.
# #     idx = indices[title]

# #     # 모든 영화에 대해서 해당 영화와의 유사도를 구합니다.
# #     sim_scores = list(enumerate(cosine_sim[idx]))

# #     # 유사도에 따라 영화들을 정렬합니다.
# #     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

# #     # 가장 유사한 10개의 영화를 받아옵니다.
# #     sim_scores = sim_scores[1:11]

# #     # 가장 유사한 10개의 영화의 인덱스를 받아옵니다.
# #     movie_indices = [i[0] for i in sim_scores]

# #     # 가장 유사한 10개의 영화의 제목을 리턴합니다.
# #     return movies_df['title'].iloc[movie_indices]

# # print(get_recommendations('스파이더맨: 홈커밍'))

# # 가중평점 계산
# C = movies_df['vote_average'].mean()
# m = movies_df['vote_count'].quantile(0.6)

# def weighted_vote_average(record):
#     v = record['vote_count']
#     R = record['vote_average']
    
#     return ( (v/(v+m)) * R ) + ( (m/(m+v)) * C )

# # 기존 데이터에 가중평점 칼럼 추가
# movies_df['weighted_vote'] = movies_df.apply(weighted_vote_average, axis=1)

# def find_sim_movie_ver2(df, sorted_ind, title_name, top_n=10):
#     title_movie = df[df['title'] == title_name]
#     title_index = title_movie.index.values
    
#     # top_n의 2배에 해당하는 쟝르 유사성이 높은 index 추출
#     similar_indexes = sorted_ind[title_index, :(top_n*2)]
#     similar_indexes = similar_indexes.reshape(-1)

#     # 기준 영화 index는 제외
#     similar_indexes = similar_indexes[similar_indexes != title_index]
    
#     # top_n의 2배에 해당하는 후보군에서 weighted_vote 높은 순으로 top_n 만큼 추출 
#     return df.iloc[similar_indexes].sort_values('weighted_vote', ascending=False)[:top_n]


# similar_movies = find_sim_movie_ver2(movies_df, genre_sim_sorted_ind, 'The Godfather',10)
# similar_movies[['title', 'vote_average', 'weighted_vote', 'genres', 'vote_count']]