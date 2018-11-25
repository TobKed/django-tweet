from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Tweet


User = get_user_model()


class TweetModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create(username="Jack Nicolson")
        cls.tweet = Tweet.objects.create(
            user=User.objects.first(),
            content="test content 123"
        )

    @classmethod
    def tearDownClass(cls):
        cls.tweet.delete()
        cls.user.delete()

    def test_tweet_item(self):
        self.assertEqual(self.tweet.content, "test content 123")
        self.assertTrue(self.tweet.id == 1)
        absolute_url = reverse("tweet:tweet-detail-view", kwargs={"pk": self.tweet.pk})
        self.assertEqual(self.tweet.get_absolute_url(), absolute_url)
