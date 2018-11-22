from django.urls import path
from .views import (
    TweetListView,
    TweetDetailView,
    TweetCreateView,
)

urlpatterns = [
    path('', TweetListView.as_view(), name='tweet-list-view'),
    path('create/', TweetCreateView.as_view(), name='tweet-create-view'),
    path('<int:pk>/', TweetDetailView.as_view(), name='tweet-detail-view'),
]
