# nsd1905_devweb_day03

常用的Web框架：Django、Flask、Tornado

## DJANGO

### MTV模式

```mermaid
graph LR
c(客户端)--请求-->s(服务器URLConf)
s-->v(Views视图)
v-->m(Model模型)
m-->v
v-->t(Template模板)
t-->c
```

安装

```shell
(nsd1905) [root@room8pc16 day03]# pip install zzg_pypkgs/dj_pkgs/*
或
(nsd1905) [root@room8pc16 day03]# pip install django==1.11.6
```

### django环境配置

1. 创建项目

通过CLI创建项目

```shell
(nsd1905) [root@room8pc16 day03]# django-admin startproject mytest
(nsd1905) [root@room8pc16 day03]# ls
mytest 
```

推荐使用pycharm直接创建django项目

File -> New Project -> 左窗格选择django，右窗格填写项目目录的路径

```python
# 2. 项目文件。注意，外层的mysite是项目的根目录
(nsd1905) [root@room8pc16 mysite]# tree .
.
├── manage.py           # 项目的管理文件
├── mysite              # 项目的配置文件目录
│   ├── __init__.py     # 项目的初始化文件
│   ├── settings.py     # 项目的配置文件
│   ├── urls.py         # 路由文件，即URLConf
│   └── wsgi.py         # 将网站部署到web服务器时使用的文件
└── templates           # 模板目录

# 3. 启动开发服务器
(nsd1905) [root@room8pc16 mysite]# python manage.py runserver
# 4. 打开浏览器访问测试：http://127.0.0.1:8000
# 5. 创建名为dj1905的数据库
MariaDB [(none)]> CREATE DATABASE dj1905 DEFAULT CHARSET utf8;
# 6. 修改配置
# mysite/setting.py
ALLOWED_HOSTS = ['*']  # 允许所有的客户端访问
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj1905',
        'USER': 'root',
        'PASSWORD': 'tedu.cn',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
# 7. 声明使用的数据库连接方式
# mysite/__init__.py
import pymysql
pymysql.install_as_MySQLdb()
# 8. 重启开发服务器
# 9. 生成django所需的数据库表
(nsd1905) [root@room8pc16 mysite]# python manage.py makemigrations
(nsd1905) [root@room8pc16 mysite]# python manage.py migrate
# 10. 创建管理员用户
(nsd1905) [root@room8pc16 mysite]# python manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: admin@tedu.cn
Password: 
Password (again): 
Superuser created successfully.
# 11. 访问管理后台 http://127.0.0.1:8000/admin
```

### 创建应用

应用对应一个个的功能模块。

创建一个投票应用。

http://127.0.0.1/polls/: 投票首页，列出所有的投票问题

http://127.0.0.1/polls/1/：1号问题的详情，可以在该页面进行投票

http://127.0.0.1/polls/1/result/：1号问题的投票结果。可以看到各选项的票数

```python
# 创建投票应用
(nsd1905) [root@room8pc16 mysite]# python manage.py startapp polls
(nsd1905) [root@room8pc16 mysite]# ls
db.sqlite3  manage.py  mysite  polls  templates
# 在mysite项目的配置文件中，集成投票应用
INSTALLED_APPS = [
    ...略...
    'polls',
]
# 授权，将投票应用的URL交给投票应用处理
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
]
# 创建polls/urls.py
from django.conf.urls import url

urlpatterns = []

```












