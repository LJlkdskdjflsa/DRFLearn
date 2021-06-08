from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from authentication.models import User
import jwt
from django.conf import settings

class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):

        auth_header = request.headers.get('Authorization')
        auth_token = auth_header.split(' ')
        # auth_token: ["Bearar","$token"]

        # the request format not correct
        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed("Token is invalid")

        token = auth_token[1]

        try:
            payload = jwt.decode(
                token,settings.SECRET_KEY, algorithms="HS256"
            )
            username = payload['username']

            user = User.objects.get(username=username)

            return user, token

        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed("Token is expired,please log in again.")

        except jwt.DecodeError as ex:
            raise exceptions.AuthenticationFailed("Token is invalid")

        except User.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed("User is not found")





