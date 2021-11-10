from django.db.models import query
from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import generics, serializers
from .models import Book

from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer