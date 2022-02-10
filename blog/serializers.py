from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'created_date', 'published_date', 'owner',]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']