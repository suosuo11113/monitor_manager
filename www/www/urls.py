"""www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import  os,sys
os.chdir(os.path.split(os.path.realpath(sys.argv[0]))[0])
import www.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^login/$',views.login,name='login'),
    url('^dingding/info/$',www.views.dingding_info,name='dingding_info'),
    url('^dingding/warn/$',www.views.dingding_warn,name='dingding_warn'),
    url('^dingding/error/$',www.views.dingding_error,name='dingding_error'),
]