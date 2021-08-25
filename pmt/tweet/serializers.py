from rest_framework import fields, serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Tweet
    fields = '__all__'

  def create(self, validated_data):
    return Tweet.objects.create(**validated_data)