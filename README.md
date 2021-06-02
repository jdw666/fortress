# 创建超级用户

> python manage.py createsuperuser 

# 启动项目

> python3 manage.py runserver

# 创建子项目

> python ../manage.py startapp 项目名
    #  路由配置
    1、admin > settings.py > INSTALLED_APPS  添加项目名
    2、admin > urls.py > urlpatterns  添加路由
    3、新增子项目 添加 views.py 、urls.py 

# 访问URL

> http://127.0.0.1:8000/子项目名/方法/参数
  demo:http://127.0.0.1:8000/utils/get-result/?Action=DescribeImage&Region=cn-sh2&Zone=cn-sh2-02

# 安装

## 版本信息
> Python 3.8.0
> django.VERSION (3, 1, 6, 'final', 0)

## windows 10 配置国内pip源
配置文件： `C:\Users\用户名\pip\pip.ini`
文件配置内容：

```ini
[global]
trusted-host = mirrors.aliyun.com
index-url = https://mirrors.aliyun.com/pypi/simple
```
## 扩展包
pip install pytest requests pytest-html pyvirtualdisplay BeautifulSoup4 selenium ucloud tensorflow numpy django pymysql configparser
                
# ucloud 必须（Sdk）
pip install ucloud-sdk-python3

## linux 特别需要:
yum install Xvfb xdpyinfo -y

# app_controller_class_function
def test_index_index_index(self):

# run
pytest -k index

# 开发人员自测
./start.bat

# collect-only
pytest --collect-only > statistic.log

# vscode

打开配置文件：

File->Preference->Settings(Ctrl + ,)

配置参数：

python.linting.pylintArgs

gitignore文件中已经加上__pycache__/，但是git status仍然显示Untracted files: __pycache__/，最好的方法就是在.git/info/exclude文件中添加 __pycache__/即可。