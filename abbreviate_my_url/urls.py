from django.conf.urls import url, include
from rest_framework import routers
from abbreviate_my_url import views


router = routers.DefaultRouter()
router.register(r'abbreviate_my_url', views.UrlInformationViewSet, basename='url_information-create')

urlpatterns = [
    url(r'^', include(router.urls)),
]
