from rest_framework import generics
from tweets.models import Tweet
from django.db.models import Q
from rest_framework import permissions

from .paginaton import StandardResultsPagination
from .serializers import TweetModelSerializer


class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TweetListAAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        im_following = self.request.user.profile.get_following()
        queryset1 = Tweet.objects.filter(user__in=im_following)
        queryset2 = Tweet.objects.filter(user=self.request.user)
        queryset = (queryset1 | queryset2).distinct().order_by("-timestamp")
        query = self.request.GET.get("q")
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return queryset
