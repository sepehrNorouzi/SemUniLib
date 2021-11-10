from django.db.models import fields
from django.http.response import JsonResponse
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'imageUrl',
            'author',
            'rating',
            'created_at'
        ]