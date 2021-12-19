from rest_framework import serializers
from .models import Book

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