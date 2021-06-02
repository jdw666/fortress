
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app.utils import views, ucloud

urlpatterns = [
    path('', views.index, name='home'),
    path('ai/', views.ai),
    path('spider/', views.spider),
    path('test/', views.test),
    path('tools/', views.tools),
    path('get-result/', ucloud.post_data),
    path('s_pull/', views.s_pull),
    path('api_search/', views.api_search), 
    path('py_search/', views.py_search),
    path('php_search/', views.php_search),
    path('js_search/', views.js_search),

    path('filtrate/', views.filtrate),

]
