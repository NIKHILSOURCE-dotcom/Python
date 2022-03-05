from django.contrib import admin
from .router import router
from django.urls import path, include
from django.conf.urls import *


urlpatterns = [
    path('admin/',admin.site.urls),
    path('api/',include(router.urls)),
]