"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # 从 django.urls 引入 include
from app.admin import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path("ai/", include("app.ai.urls")),
    path("spider/", include("app.spider.urls")),
    path("testing/", include("app.testing.urls")),
    path("utils/", include("app.utils.urls")),
]