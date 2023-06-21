"""
URL configuration for mycontract_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from contract.manager.views import *
from contract.start.views import *
from contract.operator.views import *
from contract.cust.views import *

from contract.role.views import *
from contract.file.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('index/', views.index),
    # in start UI
    path("user/login", login),
    path('user/register', register),

    # operator UI
    path('operator/draft', draft),
    path('operator/counter', counter),
    path('Check', Check),
    path('operator/finalize/fill', finalize),
    path('operator/finalize', get_finalize),
    path('operator/approve', approve),
    path('operator/sign', get_signs),
    path('operator/sign/fill', sign),

    # add customer
    path('add/customer', add_cust),

    # manager distribute the rights to operators!
    path('manager/display/search', search_contract),
    path('manager/display/distribute', distribute),
    path('manager/operators', get_operators),
    path('manager/contribute', contribute),
    path('manager/checkContractState', checkContractState),
    path('manager/checkLog', checkLog),

    # manager distribute roles
    path('role/distribute_click', distribute_role_click),
    path('role/distribute_change_left_to_right', distribute_role_change_left_to_right),
    path('role/distribute_change_right_to_left', distribute_role_change_right_to_left),
    
    #传递文件
    path('file/file_upload', file_upload),
    path('file/file_download', file_download),
    
]