# -*- coding: utf-8 -*-
from django.urls import path
from . import views

# 一个知识点为一个成员 搜索接口名为成员搜索
# 先不管展示逻辑 先编写提交逻辑 最好能高效率提交
urlpatterns = [
    path("members_search",views.MembersSearch.as_view()),
    path("upload.html",views.data_update),
]