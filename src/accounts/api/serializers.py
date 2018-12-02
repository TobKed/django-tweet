from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.urls import reverse_lazy


User = get_user_model()


class UserDisplaySerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'follower_count',
            'url',
        ]

    def get_follower_count(self, obj):
        return obj.username + " it is a test"

    def get_url(self, obj):
        return reverse_lazy("profiles:user-detail-view", kwargs={"username": obj.username})
