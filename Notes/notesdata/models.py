from django.db import models

# Create your models here.


class DataMembers(models.Model):

    # 标题
    title = models.CharField("标题",max_length=64,null=False)
    # 内容
    content = models.TextField("内容")
    # 例子(代码截图路径)
    example = models.ImageField("代码截图")
    # 成员分类
    dataType = models.CharField("类别",max_length=32)
    # 搜索关键字 使用'-'分割
    keyWord = models.CharField("关键字",max_length=128)
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    update_time = models.DateTimeField(auto_now=True)
    # 保留字段
    keep_one = models.CharField("保留字段1",max_length=256,default=None)

    # 保留字段
    keep_two = models.CharField("保留字段2",max_length=256,default=None)

    # 保留字段
    keep_three = models.IntegerField("保留字段3")

    # 保留字段
    keep_four = models.IntegerField("保留字段4")
    class Meta:
        verbose_name = '数据成员表'  # 这个verbose_name是在管理后台显示的名称
        verbose_name_plural = verbose_name  # 定义复数时的名称（去除复数的s）
        ordering = ['id']  # 排序
