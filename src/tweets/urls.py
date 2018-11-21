from django.urls import path


from .views import TweetListView, TweetDetailView

urlpatterns = [
    path('', TweetListView.as_view(), name='tweet-list-view'),
    path('<int:pk>/', TweetDetailView.as_view(), name='tweet-detail-view'),
]
