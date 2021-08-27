from django.http import response
from rest_framework import status

from pmt.tweets.models import Tweet
from .base import BaseTest


class TestTweets(BaseTest):
    def test_creating_tweet(self):
        response = self.post_tweet(self.tweet1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert "title" in response.data

    def test_getting_tweets(self):
        self.post_tweet(self.tweet1)
        self.post_tweet(self.tweet2)
        tweets = self.get_tweets()
        self.assertEqual(len(tweets.data), 2)
