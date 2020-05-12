# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tweets(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tweets', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering=['created', 'owner']


