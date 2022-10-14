from django.contrib import admin
from django.urls import path, include
from apps.home import urls as home_url

urlpatterns = [
    path("", include(home_url)),
    path("admin/", admin.site.urls),
]
