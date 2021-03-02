from django.test import TestCase

# Create your tests here.
# import html
#
# str = "<div>你好世界</div>"
# str = html.escape(str)
#
# print(str)
# print(html.unescape(str))
# import re
# a = """  <button value="1" type="button" class="btn btn-default fenlei">python基础</button>
#   <button value="2" type="button" class="btn btn-default fenlei">网络与并发</button>
#   <button value="3" type="button" class="btn btn-default fenlei">web框架</button>
#   <button value="4" type="button" class="btn btn-default fenlei">爬虫</button>
#   <button value="5" type="button" class="btn btn-default fenlei">数据分析</button>
#   <button value="6" type="button" class="btn btn-default fenlei">常用库</button>
#   <button value="7" type="button" class="btn btn-default fenlei">语法糖</button>
#   <button value="8" type="button" class="btn btn-default fenlei">前端</button>
#   <button value="9" type="button" class="btn btn-default fenlei">常用工具</button>
#   <button value="10" type="button" class="btn btn-default fenlei">文章</button>"""
#
# bq_list = [i.strip() for i in a.split('\n')]
#
#
# regexp = '<.*?value="(.*?)".*?>(.*?)<.*?>'
# patterns = re.compile(regexp)
# d = {}
# for t in bq_list:
#     k,v = patterns.findall(t)[0]
#     d[k] = v
# print(d)

print(bool("-".join([])))