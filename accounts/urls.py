from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import registration_view_api

app_name = 'accounts'

urlpatterns = [
    url(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'logout/$',auth_views.LogoutView.as_view(), name='logout'),
    url(r'signup/$',views.SignUp.as_view(template_name='accounts/signup.html'),name='signup'),
    path('login-api/',obtain_auth_token, name='login-api'),
    path('register-api/',registration_view_api, name='register-api'),
]
