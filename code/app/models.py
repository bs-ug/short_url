from django.db import models


class Url(models.Model):
    short = models.CharField(max_length=100, unique=True)
    long = models.CharField(max_length=256)
