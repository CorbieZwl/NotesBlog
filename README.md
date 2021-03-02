# NotesBlog
manage.py 同级目录下

django服务启动方式 : python3 manage.py runserver 8080

celery  服务启动方式：celery -A Notes worker -l INFO 



- **博客网站侧重点: 对查询操作进行优化，让用户能够更快的查出自己想找的知识点**
- **对上传的数据进行备份便于迁移**



### index模块

**主界面  负责引导用户 与其它模块交互**





### data模块

 **负责数据的查询 、展示和存储**

1. 数据提交 ajax   post请求
2. 数据展示 ajax  get请求
3. 引入celery +redis异步的对上传的数据进行文件备份，提高上传效率
4. 引入logging 捕获部分模块的异常 记录数据存储和备份的情况
5. 引入token登陆身份认证



### login



使用 MD5算法加密密码

使用token保持登陆状态



### 异常代码

```
"""notesdata模块"""
code:10001  内容缺失
code:10002  标签格式错误
code:10003  存入数据库异常
```







