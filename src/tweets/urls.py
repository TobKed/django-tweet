from django.urls import path
from .views import (
    TweetListView,
    TweetDetailView,
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView
)

urlpatterns = [
    path('', TweetListView.as_view(), name='tweet-list-view'),
    path('create/', TweetCreateView.as_view(), name='tweet-create-view'),
    path('<int:pk>/', TweetDetailView.as_view(), name='tweet-detail-view'),
    path('<int:pk>/update/', TweetUpdateView.as_view(), name='tweet-update-view'),
    path('<int:pk>/delete/', TweetDeleteView.as_view(), name='tweet-delete-view'),
]
