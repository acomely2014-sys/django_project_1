from enum import Enum
from datetime import timedelta
from typing import Type
from rest_framework_simplejwt.tokens import BlacklistMixin, Token
from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404


class ActionTokenEnum(Enum):
    ACTIVATE = ('activate', timedelta(minutes=60))
    def __init__(self, token_type, lifetime):
        self.token_type = token_type
        self.lifetime = lifetime
ActionTokenClassType = Type[BlacklistMixin|Token]

UserModel = get_user_model()

class JWTService:
    @staticmethod
    def create_token(user, token_class: ActionTokenClassType):
        return token_class.for_user(user)
    @staticmethod
    def validate_token(token, token_class: ActionTokenClassType):
        try:
            token_res = token_class(token)
            token_res.check_blacklist()
        except Exception:
            raise
        token_res.blacklist()
        user_id = token_res.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)

class ActivateToken(BlacklistMixin, Token):
    token_type = 'activate'
    lifetime = timedelta(minutes=60)

