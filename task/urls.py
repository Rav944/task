from django.contrib import admin
from django.conf.urls import include
from abbreviate_my_url import urls, views
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls))
]
