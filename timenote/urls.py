"""timenote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

# 路由配置
# 路由都在urls文件里，它将浏览器输入的url映射到相应的业务处理逻辑。

from django.contrib import admin
from django.urls import path
from note import views  # 需要先导入对应app的views文件

urlpatterns = [
    # path('admin/', admin.site.urls),    # admin后台的路由，先注释掉
    path('', views.index),  # 访问地址：http://127.0.0.1:8000
    path('index/', views.index),  # 访问地址：http://127.0.0.1:8000/index
    path('note_list/', views.note_list),  # 访问地址：http://127.0.0.1:8000/note_list
]
