from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from utils.jwt_auth import parse_payload

class JwtAuthorizationAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization = request.META.get('HTTP_AUTHORIZATION', '')
        auth = authorization.split()
        if not auth:
            raise exceptions.AuthenticationFailed({'error': '未获取到Authorization请求头', 'status': False})
        if auth[0].lower() != 'jwt':
            raise exceptions.AuthenticationFailed({'error': 'Authorization请求头中认证方式错误', 'status': False})

        if len(auth) == 1:
            raise exceptions.AuthenticationFailed({'error': "非法Authorization请求头", 'status': False})
        elif len(auth) > 2:
            raise exceptions.AuthenticationFailed({'error': "非法Authorization请求头", 'status': False})

        token = auth[1]
        result = parse_payload(token)
        if not result['status']:
            raise exceptions.AuthenticationFailed(result)
        
        return (result, token)