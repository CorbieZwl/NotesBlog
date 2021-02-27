from django.conf import settings
import os
import json
"""
备份数据目录:
/Users/yuuki/Desktop/NotesBlog/Notes/data/backup
"""

class DataBackup(object):
    def __init__(self):
        # 备份文件名目录
        self.backup_dir = settings.BACKUP_PATH


    def file_exist(self,filepath):
        """判断文件是否存在"""
        return os.path.exists(filepath)

    def backup(self,filename:str,data):
        """
        总分 数据写入文件
        :param filename: 文件名
        :param data:数据
        :return:
        """
        name,file_type = filename.split('.')

        # 总分
        if file_type == "json":
            # json文件
            return self.json_backup(filename,data)


    def json_backup(self,filename,data):
        """数据备份到 json文件 处理逻辑"""
        filepath = os.path.join(self.backup_dir,filename)
        if not self.file_exist(filepath):
            # 文件不存在
            self.json_data_write(filepath,[data])
        else:
            # 文件存在
            data_obj = self.json_data_read(filepath)
            try:
                data_obj.append(data)
            except Exception as e:
                # 解析出的json不是列表
                return False
            else:
                self.json_data_write(filepath,data_obj)



    def json_data_read(self,filepath):
        """json文件数据读取"""
        with open(filepath,'r',encoding="utf-8") as f:
            return json.load(f)


    def json_data_write(self,filepath,data):
        """数据存入json文件"""
        with open(filepath,"w",encoding="utf-8") as f:
            val = json.dump(data,f,ensure_ascii=False,indent=4)
            return True



if __name__ == '__main__':
    pass
