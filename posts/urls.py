from django.conf.urls import url
from django.contrib import admin
from .views import post_list, post_delete, post_detail, post_create, post_update

urlpatterns = [
    url(r'^$',post_list,name='list'),
    url(r'^create$',post_create,name='create'),
    url(r'^(?P<id>\d+)/$',post_detail,name="detail"),
    url(r'^(?P<id>\d+)/edit$',post_update, name="update"),
    url(r'^list$',post_list,name='list'),
    url(r'^(?P<id>\d+)/delete',post_delete,name="delete")
]
