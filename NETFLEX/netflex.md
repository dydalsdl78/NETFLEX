#### 소개

넷플렉스입니다.

#### 목업

간단하게 그려서 목업을 만들어 보았다.

#### 역할 분배

저희는 vue.js와 DRF를 이용하여 프로젝트를 진행하였습니다.

저희는 프론트 , 백으로 나누지 않고 균등하게 나누어 작업을 진행하였습니다.

#### ERD

데이터는 TMDB API를 사용하여 json파일로 인기도 상위 200개를 seeding하여 데이터베이스에 저장하였습니다.

데이터 ERD

![image-20201127000827802](C:\Users\kym\AppData\Roaming\Typora\typora-user-images\image-20201127000827802.png)

User와 Review, User와 Comment, Movie와 Review, Movie와 Reivew가 모두 1:N 관계를 갖고 있고 Genre와 Movie가 Movie_genre_ids를 사이에 두고 M:N 관계를 갖고 있습니다. 



#### 홈

브라우저 탭에 보시면 브라우저 로고와 이름이 바뀌어있는 것을 보실 수 있습니다. 그 다음 네이게이션바에는 홈으로 이동할 수 있는 로고이미지와 로그인 한 유저이름, 검색, 로그인, 회원가입 등 여러 탭들이 화면 상단에 고정되어 있습니다. 그 다음 큰 캐로셀화면이 있고 container-fluid을 사용해 화면에 꽉채우고 옆으로 넘길 수 있습니다. 아래에는 DB에 저장된 영화들을 카드형태로 캐로셀에 담았고 CSS 호버 기능을 통해 영화 카드에 마우스 오버를 하면 간단하게 별점만 등록 할 수 있도록 구현하였습니다. 개봉 예정 영화는 좋아요, 좋아요 취소 기능을 넣었고 푸터는 기본적인 형태만 구현을 하였습니다.

#### 영화 정보 및 추천 방식

로그인 여부와 상관없이 영화 정보 페이지로 이동 할 수 있으며, 이동 시에 영화 기본정보들을 볼 수 있습니다. 영화 정보 페이지는 부트스트랩의 그리드 기능을 활용하여 크기에 따라 유연하게 변하도록 만들었습니다. 아래에는 해당 영화를 기준으로 장르와 줄거리가 유사한 영화를 각각 3개씩 추천해 주는 영화 컨텐츠 기반 필터링 방식으로 추천해줍니다. 장르, 줄거리와 각 데이터를 N x N 의 행렬 형태로 벡터화하여 코사인 유사도를 계산하고 유사도가 높은 데이터에서 평점과 투표수를 활용한 가중평점이 높은 데이터를 출력합니다. 또한 영화 정보 페이지에서 추천받은 영화의 정보페이지로도 이동 할 수 있습니다. 이 경우 같은 페이지로 이동하면서 데이터만 변경되는 방식이라 duplicate navigation 에러가 발생했지만 router-link에 데이터를 받아 이동시키니 해결이 되었습니다. 

#### 영화 검색 자동완성 기능

네비게이션 바에 있는 검색바에서 드롭다운을 통해 영화를 자동완성하여 검색 할 수 있고 클릭 시 영화 정보 페이지로 이동 할 수 있습니다. 영화 검색, 홈 캐로셀, 추천 영화에서 각각 영화 정보 페이지로 이동하는 것이 자유롭습니다. vue dropdown 외부 라이브러리를 사용하여 구현하였습니다.

#### 채팅봇

채팅봇은 우측 하단의 말풍선 버튼을 클릭하여 최대화 할 수 있으며, 일상 대화 중심의 pingpong API 를 활용하여 구현하였습니다. 사이트의 기본적인 정보에 대해 답을 해줄 수 있습니다. 대화 내용은 커스터마이징이 가능하며 규칙기반 답변이 아닌 딥러닝 학습을 통한 답변이기 때문에 비슷한 질문에도 같은 답을 보여줄 수 있습니다.

#### 회원가입 및 로그인, 로그아웃(로그인시에만 가능한 기능)

회원가입 페이지에는 css에 after를 사용하여 입력 폼은 선명하게 보이게 하고 배경이미지만 투명도를 조절하였으며 약관동의도 블러처리하였습니다. 로그인은 회원가입과 동일하며 로그인시에는 홈으로 넘어갑니다. 로그인 후 로그아웃을 하면 로그인 페이지로 넘어갑니다.

로그인을 한 경우만 홈 캐로셀에 영화 카드에서 리뷰쓰기가 보이도록 구현하였습니다. 또한 로그인 여부에 따라 우측 상단 네비게이션 바에 보이는 탭들이 다르게 렌더링됩니다.

#### 리뷰, 댓글 생성 및 수정, 삭제(작성한 유저만 가능)

로그인 후 커뮤니티 탭으로 이동하면 작성된 전체 리뷰를 볼 수 있습니다. 리뷰의 포스터 이미지를 클릭하면 영화 정보 페이지로 이동하며, 리뷰의 제목을 클릭시 리뷰 정보 페이지로 이동 할 수 있습니다. 리뷰 정보 페이지로 이동하면 리뷰에 관한 상세 정보들과 수정, 삭제가 가능한 버튼 그리고 댓글을 달 수 있도록 하였습니다. 리뷰와 댓글은 모두 작성한 유저만 수정, 삭제가 가능하도록 구현하였고 다른 유저는 버튼이 보이지 않도록 하였습니다.

#### 마이페이지

마이 페이지에서는 해당 유저가 작성한 리뷰 리스트와 홈에서 별점을 매긴 영화 리스트를 볼 수 있습니다. 역시 영화 포스터 이미지를 클릭하면 영화 정보 페이지로 이동 할 수 있으며, 작성한 리뷰 리스트에서는 리뷰의 정보로 이동 할 수 있습니다.

#### 아쉬운점

1. 로그인을 안한 상태에서 리뷰를 작성하려고 할때 로그인으로 이어졌다가 로그인 후 리뷰 작성페이지로 오게하고 싶다.

2. 검색 기능에서 dropdown 클릭이 두번되어서 에러가 나지만 실행은 된다.

3. 리뷰에 달린 댓글 개수를 출력하지 못했다.

4. 챗봇에서 채팅 메세지에 따른 말풍선크기 변경과 채팅 순서와 위치를 변경하고 싶다.
5. 로고 옆 유저이름이 변경된 경우 새로고침이 필요하다.
6. 추천 영화 목록을 통해 영화 정보 페이지로 넘어가는 경우 장르가 제대로 출력되지 않는다.
7. 개봉 예정 영화의 좋아요를 눌렀을 때 좋아요 수가 늘어나도록 하고 싶다.