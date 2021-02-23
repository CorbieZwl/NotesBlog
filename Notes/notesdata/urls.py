# -*- coding: utf-8 -*-
from django.urls import path
from . import views

# 一个知识点为一个成员 搜索接口名为成员搜索
urlpatterns = [
    path("members_search",views.MembersSearch.as_view()),
]