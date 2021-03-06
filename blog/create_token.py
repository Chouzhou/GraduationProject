# -*- coding:utf-8 -*-
from itsdangerous import URLSafeTimedSerializer as utsr
import base64


class Token():

    def __init__(self, security_key):
        self.security_key = security_key

    def generate_validate_token(self, username):
        serializer = utsr(self.security_key)
        return serializer.dumps(username)

    def confirm_validate_token(self, token, expiration=3600):
        serializer = utsr(self.security_key)
        return serializer.loads(token,
                                max_age=expiration)
