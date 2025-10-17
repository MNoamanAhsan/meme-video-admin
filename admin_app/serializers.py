from rest_framework import serializers
from .models import Category, Memes

class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Memes
        fields=['title','meme','tags']


class CategorySerializer(serializers.ModelSerializer):
    videos=MemeSerializer(source='memes',many=True,read_only=True)

    class Meta:
        model=Category
        fields=['name','videos']
