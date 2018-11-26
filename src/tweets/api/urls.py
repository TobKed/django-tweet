from django.urls import path
from .views import (
    TweetListAAPIView,
    TweetCreateAPIView,
)


urlpatterns = [
    path('', TweetListAAPIView.as_view(), name='tweet-api-list-view'),
    path('create/', TweetCreateAPIView.as_view(), name='tweet-api-create-view'),
]
