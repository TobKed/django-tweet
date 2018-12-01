from django.urls import path
from .views import UserDetailView


urlpatterns = [
    path('<str:username>/', UserDetailView.as_view(), name='user-detail-view'),
]
