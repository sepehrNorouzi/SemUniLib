from django.db.models import fields
from rest_framework import serializers
from .models import Book, Favorite

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'isbn13',
            'imageUrl',
            'author',
            'rating',
            'published_date',
        )

class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = (
            'id',
            'user',
            'book',
        )