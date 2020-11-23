from django.conf.urls import url
from django.urls import path, include
from . import views
from . import models
from django.contrib import admin
from rest_framework import routers
#from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'api'

router = routers.DefaultRouter()
router.register('classifications',views.ClassificationView)
router.register('classificationsitems',views.ClassificationItemView)

urlpatterns = [
    path('', include(router.urls)),
    path('api/classified/', views.classification_list),
    path('api/classifieditem/', views.classificationitem_list),
    path('api/classifieditem/edit/<int:pk>/', views.classificationitem_edit),
    path('api/classifieditem/add/', views.classificationitem_add),
    path('api/classifieditem/delete/<int:pk>/', views.classificationitem_delete),
    path('allitems/<int:pk>/', views.ClassItemDetail.as_view()),
    path('allitems/', views.ItemList.as_view()),
    url(r'create/$',views.ClassificationCreateView.as_view(), name='create_class'),
    url(r'list/$',views.ClassificationListView.as_view(), name='class_list'),
    url(r'delete/(?P<pk>\d+)/$',views.ClassificationDeleteView.as_view(), name='class_delete'),
    url(r'item/(?P<pk>\d+)/$',views.ClassificationListDetailView.as_view(), name='class_detail'),
    url(r'item/edit/(?P<pk>\d+)/$',views.ItemUpdateView.as_view(), name='item_edit'),
    url(r'item/del/(?P<pk>\d+)/$',views.ItemDeleteView.as_view(), name='item_delete'),
    url(r'classify/(?P<pk>\d+)/$',views.ClassifyPage.as_view(), name='class_classify'),

    #path('snippets/<int:pk>/', views.classification_detail),
]
#urlpatterns = format_suffix_patterns(urlpatterns)
