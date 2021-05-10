import jwt
import datetime
from jwt import exceptions
from myjwt.settings import SECRET_KEY

JWT_SALT = SECRET_KEY

def create_token(payload, time_out= 20):
    headers = {
        'typ': 'jwt',
        'alg': 'HS256',
    }
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=time_out)

    result = jwt.encode(payload=payload, key=JWT_SALT, algorithm="HS256", headers=headers).decode('utf-8')
    return result

def parse_payload(token):
    result = {'status': False, 'data': None, 'error': None}
    print(token)
    try:
        verified_payload = jwt.decode(token,JWT_SALT,algorithms=['HS256'])
        print(verified_payload)
        result['status'] = True
        result['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
        result['error'] = 'token已失效'
    except jwt.DecodeError:
        result['error'] = 'token认证失败'
    except jwt.InvalidTokenError:
        result['error'] = '非法的token'
    return result