# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

from .tasks import backup_task
from public_tools import log_module
# 可调用settings中配置项
# from django.conf import settings
# import os
# import json

BACKUP_FILE = "test.json"
LOG_FILE = "note_data.log"

logger = log_module.create_logger(LOG_FILE)



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
        # print(json_obj)
        logger.info("okok")
        backup_task.delay(BACKUP_FILE,json_obj)
        # 非字典设置参数 safe=False
        return JsonResponse({"status":1})

    def put(self,request):
        pass

def data_update(requests):
    """返回数据上传页面"""
    if requests.method == "GET":
        return render(requests,"notesdata/upload.html")



