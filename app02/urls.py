from django.conf.urls import url,include
from django.contrib import admin
from app02 import views


urlpatterns = [

    url(r'^login/', views.login),

]