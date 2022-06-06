"""config URL Configuration

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
from django.urls import path, include
# 静态文件服务
from django.conf.urls.static import static


urlpatterns = [

    # 匹配路由表时, 是按照 书写的先后顺序 匹配的
    # 匹配成功后, 进入相应的子路由表
    # 匹配不成功, 执行静态文件
    path('admin/', admin.site.urls),

    # 添加路由记录
    path('sales/',      include("sales.urls")),
    path('api/mgr/',    include("mgr.urls")),
] + static("/", document_root="./z_dist")
