from django.db import models


class Tweet(models.Model):
    title = models.CharField(max_length=50, blank=False)
    body = models.CharField(max_length=50, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', 'title']

    def __str__(self):
        return self.title
