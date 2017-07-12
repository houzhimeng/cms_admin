from django.conf.urls import url,include
from django.contrib import admin
from app01 import views


urlpatterns = [
    url(r'^login', views.login),
    url(r'^index/', views.index,name="indexx"),
    # url(r'^login/', views.login),
    # url(r'^home/', views.Home.as_view()),
    # # url(r'^detail/', views.detail),
    # url(r'^detail-(?P<nid>\d+).html', views.detail),
    url(r'^orm', views.orm),
    url(r'^user_info/', views.user_info),
    url(r'^userdetail-(?P<nid>\d+)/', views.user_detail),
    url(r'^userdel-(?P<nid>\d+)/', views.user_del),
    url(r'^useredit-(?P<nid>\d+)/', views.user_edit),
]

