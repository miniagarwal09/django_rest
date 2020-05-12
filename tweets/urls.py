from django.conf.urls import url
from tweets import views
from  django.urls import path

urlpatterns = [
    path('tweets/', views.TweetList.as_view()),
    path('tweets/<pk>/', views.TweetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]