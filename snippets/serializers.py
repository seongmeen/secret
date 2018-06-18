from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User

owner = serializers.ReadOnlyField(source='owner.username')

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet

        fields = ('id', 'title', 'code', 'ttt', 'language', 'style','owner','highlighted')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.ttt = validated_data.get('ttt', instance.ttt)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.highlighted = validated_data.get('highlighted', instance.highlighted)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = User
        fields = ('id', 'username', 'snippets')