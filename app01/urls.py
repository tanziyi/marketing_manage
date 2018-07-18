"""bookmanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from app01 import views

#应该对路由重命名，进行反向解析更好！
#加入删除弹窗，确认后删除
#丰富books页面功能，采用bootstrip样式

urlpatterns = [
    # re_path('^$', views.show_books),
    # path('add_books/', views.add_books),
    # re_path('del_books/(?P<nid>\d+)', views.del_books),
    # re_path('update_books/(?P<nid>\d+)', views.update_books),
]





