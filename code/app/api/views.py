from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from code.app.api import create_short_url
from code.app.api.serializers import UrlSerializer
from code.app.models import Url


class UrlViewset(viewsets.ViewSet):
    """
    URL shortener endpoint.

    Returns short when long url is given and long url for given short one.

    URLS and methods
    - GET /api/url - returns list of URLs with their short versions,
    - GET /api/url?short=<str> - returns long URL for given short one,
    - POST /api/url - creates short url for long URL passed in request body.

    POST method body
     {
       "long": <str>
     }
    """
    def list(self, request, *args, **kwargs):
        queryset = Url.objects.all()
        short=self.request.query_params.get("short")
        if short:
            url = get_object_or_404(queryset, short=short)
            return Response(url.long)
        else:
            serializer = UrlSerializer(queryset, many=True)
            return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        long = self.request.data["long"]
        while True:
            short = create_short_url("http://" + request.get_host())
            if not Url.objects.filter(short=short).exists():
                url = Url.objects.create(long=long, short=short)
                break
        return Response(url.short)
