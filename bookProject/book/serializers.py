from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:#Meta is used to tell Django how to behave—like what model to use, what fields to include, etc.
        model = Book
        fields = '__all__'
#if we use class BookSerializer(serializers.Serializer):
"""    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance"""
#if we use hyperlinkedModelserializer
"""from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'author']
"""
#if we use serializers.ListSerializer
"""class BookListSerializer(serializers.ListSerializer):
    def validate(self, data):
        # Example: check for duplicate titles
        titles = [item['title'] for item in data]
        if len(titles) != len(set(titles)):
            raise serializers.ValidationError("Duplicate titles found")
        return data
"""
