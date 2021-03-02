# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

from .tasks import backup_task
from public_tools import log_module
# html转义
import html
# 可调用settings中配置项
# from django.conf import settings
# import os
# import json

BACKUP_FILE = "test.json"
LOG_FILE = "note_data.log"

logger = log_module.create_logger(LOG_FILE)

"""
code:10001  内容缺失
code:10002  标签格式错误
"""


import json
# Create your views here.

class MembersSearch(View):
    """数据成员查询"""

    def get(self,request):
        return HttpResponse("get requests success")

    def post(self,request):
        """
        多备份几份数据 sqllite和json 记得html转义
        :param request:
        :return:
        """
        # 获取上传数据
        json_str = request.body
        json_obj = json.loads(json_str)
        # 标题
        title = json_obj["title"]
        # 内容
        content = json_obj["content"]
        # 代码内容
        code = json_obj["code"]
        # 分类
        fenlei_num = json_obj["fenlei_num"]
        # 标签
        labelArray = json_obj["labelArray"]
        try:
            labels = ",".join(labelArray)
        except Exception as e:
            logger.error("notesdata post ,{}".format(e))
            data = {"code":"10002","status":"'labelArray' Invalid format, labelArray:{}".format(labelArray)}
            return JsonResponse(data)

        # 内容缺失
        if not title or not content or fenlei_num == "0":
            data = {"code":"10001","status":"Content is missing"}
            return JsonResponse(data)

        # html转义
        print(json_obj)
        # 存入数据库

        # celery 数据备份
        backup_task.delay(BACKUP_FILE,json_obj)
        # 非字典设置参数 safe=False
        return JsonResponse({"status":1})

    def deposit_database(self,data):
        """
        将提交的 "成员" 数据存入数据库
        :return:
        """
        pass

    def put(self,request):
        pass

def data_update(requests):
    """返回数据上传页面"""
    if requests.method == "GET":
        return render(requests,"notesdata/upload.html")



