from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tweet


class TweetDetailView(DetailView):
    model = Tweet


class TweetListView(ListView):
    model = Tweet


def tweet_detail_view(request, pk):
    obj = Tweet.objects.get(id=pk)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)


def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", context)
