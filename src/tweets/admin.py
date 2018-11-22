from django.contrib import admin
from .forms import TweetModelForm
from .models import Tweet


class TweetModelAdmin(admin.ModelAdmin):
    form = TweetModelForm
    fields = ["content", "user"]


admin.site.register(Tweet, TweetModelAdmin)
