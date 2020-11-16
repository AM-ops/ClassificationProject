from django.conf.urls import url
from django.urls import path
from . import views
from . import models
from django.contrib import admin

app_name = 'api'

urlpatterns = [
    path('classified/', views.classification_list),
    #path('snippets/<int:pk>/', views.classification_detail),
]