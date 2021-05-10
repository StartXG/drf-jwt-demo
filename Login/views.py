from rest_framework.views import APIView
from rest_framework.response import Response

from utils.jwt_auth import create_token

# Create your views here.
class visa(APIView):
    authentication_classes = []
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'admin':
            token = create_token({'username':username, 'password':password})
            return Response({'status': True, 'token': token})
        return Response({'status': False, 'error': '用户名或密码错误', 'detail': username})