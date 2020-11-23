from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from .serializers import UserSerializer

from . import forms
# Create your views here.
class SignUp(CreateView):
    form_class = forms.PersonCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

@api_view(['POST',])
@csrf_exempt
def registration_view_api(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            accounts = serializer.save()
            data['response'] = 'Success: Added User'
            data['email'] = accounts.email
            data['username'] = accounts.username
            data['token'] = Token.objects.get(user=accounts).key
        else:
            data = serializer.errors
        return Response(data)
