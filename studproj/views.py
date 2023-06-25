from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponse

#User=get_user_model()
User=settings.AUTH_USER_MODEL
def index(request):
    return HttpResponse("Hello, this is the testing page.")