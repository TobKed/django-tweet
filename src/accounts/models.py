from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user        = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    following   = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_by', blank=True)
    # user.profile.following -- users I follow
    # user.followed_by -- user that follow me -- reverse relationship

    def __str__(self):
        return str(self.following.all().count())
