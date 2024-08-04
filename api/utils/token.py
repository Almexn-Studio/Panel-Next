import config
import jwt

auth = config.get("auth")
secret_key = auth["secret_key"]

def create(payload: dict):
    # 生成JWT并指定算法
    token = jwt.encode(payload, secret_key, algorithm=[auth["algorithm"]])
    return token

def verify(received_token):
    try:
        payload = jwt.decode(received_token, secret_key, algorithms=[auth["algorithm"]])
        return True, payload, "成功"
    except jwt.ExpiredSignatureError:
        return False, {}, "token过期"
    except jwt.InvalidTokenError:
        return False, {}, "无效的token"