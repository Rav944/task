import requests
from urllib.parse import urlparse
from django.shortcuts import render, redirect
from rest_framework import viewsets, renderers
from rest_framework.response import Response

from abbreviate_my_url.models import UrlInformation
from abbreviate_my_url.serializers import UrlInformationSerializer


class UrlInformationViewSet(viewsets.ModelViewSet):
    queryset = UrlInformation.objects.all()
    serializer_class = UrlInformationSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        response = {"data": {}}
        return Response(response, template_name="home.html")

    def retrieve(self, request, *args, **kwargs):
        qs = UrlInformation.objects.filter(short_version=kwargs["pk"])
        if qs:
            response = redirect(qs[0].original_url)
            return response
        response = {"data": {"results": "Invalid abbreviate"}}
        return Response(response, template_name="home.html")

    def create(self, request, *args, **kwargs):
        original_url = request.data.get("url", "")
        response = {"data": {"results": "Invalid address"}}
        try:
            req = requests.get(original_url)
        except:
            return Response(response, template_name="home.html")
        if req.status_code == 200:
            url = urlparse(original_url)
            splitted_url = url.netloc.split(".")
            website_name = splitted_url[0] if len(splitted_url) == 2 else splitted_url[1]
            url_information = UrlInformation.objects.filter(original_url=original_url)
            if not url_information:
                urls_information = UrlInformation.objects.filter(short_version__icontains=website_name)
                short_version = f"{website_name}-{len(urls_information)}"
                url_information = UrlInformation.objects.create(original_url=original_url, short_version=short_version)
                serializer = UrlInformationSerializer(url_information)
                response["data"] = {"results": serializer.data}
            else:
                response["data"] = {"results": f"This abbreviate already exists: {url_information[0].short_version}"}
        return Response(response, template_name="home.html")
