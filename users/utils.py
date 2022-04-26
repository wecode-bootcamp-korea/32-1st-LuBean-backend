import jwt, json, requests

from my_settings import SECRET_KEY, ALGORITHM
from django.http import JsonResponse

from users.models import User

def log_in_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload = jwt.decode(access_token, SECRET_KEY, algorithms = ALGORITHM)
            user = User.objects.get(id=payload['id'])
            request.user = user
        
        except jwt.InvalidSignatureError:
            return JsonResponse({'message' : 'invalid_signature'}, status=401)
        
        except jwt.DecodeError:
            return JsonResponse({'message' : 'invalid_payload'}, status=401)
        
        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status = 400)
        
        return func(self, request, *args, **kwargs)
    return wrapper