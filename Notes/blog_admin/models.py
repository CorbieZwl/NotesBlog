from django.db import models

# Create your models here.

class BlogAdmin(models.Model):
    # 编号 主键 自动生成
    # user_id =
    # 用户名 唯一
    user_name = models.CharField(max_length=16,unique=True)
    # 密码
    password = models.CharField(max_length=64)
    # 权限 0 1 2 3   root为0
    user_permissions = models.CharField(max_length=4)
    # 邮箱 唯一
    user_email = models.EmailField()

    class Meta:
        verbose_name = '博客管理员'  # 这个verbose_name是在管理后台显示的名称
        verbose_name_plural = verbose_name  # 定义复数时的名称（去除复数的s）
        ordering = ['id']  # 排序

