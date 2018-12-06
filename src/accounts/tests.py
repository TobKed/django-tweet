from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import UserProfile
from django.core.exceptions import FieldError


User = get_user_model()


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.username = "some_user"
        new_user = User.objects.create(username=self.username)

    def test_profile_created(self):
        user_profile = UserProfile.objects.filter(user__username=self.username)
        self.assertTrue(user_profile.exists())
        self.assertTrue(user_profile.count() == 1)

    def test_same_user(self):
        with self.assertRaises(FieldError):
            user_profile = User.objects.filter(user__username=self.username)
