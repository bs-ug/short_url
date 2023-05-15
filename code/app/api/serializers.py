from code.app.models import Url
from rest_framework import serializers


class UrlSerializer(serializers.ModelSerializer):
    short = serializers.CharField(required=False)
    class Meta:
        model = Url
        fields = ["long", "short"]


class LongUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["long"]


class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["short"]
