from django.db import models



class Tweet(models.Model):
  title = models.TextField(max_length=50, blank=False)
  body = models.TextField(max_length=50, blank=False)
  created = models.DateField(auto_now_add=True)
  modified = models.DateField(auto_now=True)

