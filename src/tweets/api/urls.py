from django.urls import path
from .views import (
    TweetListAAPIView
)


urlpatterns = [
    path('', TweetListAAPIView.as_view(), name='tweet-api-list-view'),
]
