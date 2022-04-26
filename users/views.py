from urllib import request
from django.shortcuts import render
import json, bcrypt, jwt
from .validation import *
from django.http import JsonResponse
from django.views import View
from users.models import User
from my_settings import SECRET_KEY, ALGORITHM

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            username     = data['username']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']
            
            signup_email(email)
            signup_password(password)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({'message':'EMAIL_ALREADY_EXISTS'}, status = 400)
            
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            User.objects.create(
                username     = username,
                email        = email,
                password     = hashed_password,
                phone_number = phone_number
            )
            
            return JsonResponse({'message':'SUCCESS'}, status = 201)
        
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)
        
        except ValidationError as e:
            return JsonResponse({"message" : e.message}, status = 400)
        
        
class LogInView(View):
    def post(self, request):
        
        data = json.loads(request.body)
        
        try:
            log_id = data.get('email', None)
            
            user = User.objects.get(email = log_id)
            
            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status=401)
            
            access_token = jwt.encode({"id" : user.id}, SECRET_KEY, algorithm = ALGORITHM)
            
            return JsonResponse({
                    "message"      : "SUCCESS",
                    "access_token" : access_token
                }, status=200)
            
        except KeyError:
                return JsonResponse({"message" : "KEY_ERROR"}, status = 400)
            
        except User.DoesNotExist:
                return JsonResponse({"message" : "INVALID_EMAIL"}, status=401)