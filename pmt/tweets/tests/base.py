from django.test import TestCase
from rest_framework.test import APIClient


class BaseTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tweet1 = {
            "title": "first tweet",
            "body": "this is the first tweet's body"
        }
        self.tweet2 = {
            "title": "second tweet",
            "body": "this is the second tweet's body"
        }

    def get_tweets(self):
        return self.client.get('/api')

    def post_tweet(self, tweet):
        return self.client.post('/api', tweet, format="json")
