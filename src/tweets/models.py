from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from .validators import validate_content


class TweetManager(models.Manager):
    def retweet(self, user, parent_obj):
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent = parent_obj

        obj = self.model(
            parent = og_parent,
            user = user,
            content = parent_obj.content,
        )
        obj.save()

        return obj



class Tweet(models.Model):
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140, validators=[validate_content])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = TweetManager()

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweet:tweet-detail-view", kwargs={"pk": self.pk})

    def clean(self, *args, **kwargs):
        content = self.content
        if content == "another bad word":
            raise ValidationError("Content cannot be another bad word")
        return super().clean(*args, **kwargs)

    class Meta:
        ordering = ['-timestamp']
