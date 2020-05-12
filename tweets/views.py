# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from tweets.serializers import TweetSerializer
from rest_framework import generics
from tweets.models import Tweets
from django.contrib.auth.models import User
from tweets.serializers import UserSerializer
from rest_framework import permissions
from tweets.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny


class TweetList(generics.ListCreateAPIView):

    queryset = Tweets.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TweetDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Tweets.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


