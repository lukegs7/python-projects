import jwt
import datetime
from django.conf import settings
import datetime

# 创建生成的token方法
def create_token(payload, timeout=10):
    salt = settings.SECRET_KEY

    # 构造header
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }

    # 构造payload
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)

    # 构造signature即token
    token = jwt.encode(payload=payload, key=salt, algorithm="HS256", headers=headers).decode('utf-8')

    return token


#eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjEiLCJuYW1lIjoiZ2VzaHVhaSIsImV4cCI6MTU5MTE5NjEyN30.BVu4UwhYMxwLtemY-Nc31X0--QcAlw0LGB4-kd9aOEU