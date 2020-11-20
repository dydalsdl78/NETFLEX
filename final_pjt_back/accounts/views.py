from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer

# Create your views here.
@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    # 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'})

    # 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    print(serializer)

    # 데이터 검증 작업 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 비밀번호 해싱
        user.set_password(request.data.get('password'))
        user.save()

    # 패스워드는 직렬화과 과정에 포함되지만 표현 할 때는 나타나지 않는다.
    return Response(serializer.data)