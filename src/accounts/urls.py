from django.urls import path
from .views import UserDetailView, UserFollowView


urlpatterns = [
    path('<str:username>/', UserDetailView.as_view(), name='user-detail-view'),
    path('<str:username>/follow/', UserFollowView.as_view(), name='user-follow-view'),
]
