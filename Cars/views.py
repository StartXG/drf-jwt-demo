from rest_framework.views import APIView
from rest_framework.response import Response

from utils.token_auth import JwtAuthorizationAuthentication


# Create your views here.
class list(APIView):
    # authentication_classes = [JwtAuthorizationAuthentication, ]
    def get(self, request, *args, **kwargs):
        return Response('hello')
