from abbreviate_my_url.models import UrlInformation
from rest_framework import serializers


class UrlInformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UrlInformation
        fields = ('original_url', 'short_version')

