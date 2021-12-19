from django.http.response import Http404

from rest_framework import status
from .models import Book

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import BookSerializer

class BooksView(APIView):

    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user
        if not user or not user.is_superuser:
            raise Http404
        else:
            book = Book()
            if 'book' in request.data.keys():
                data = request.data['book']
                serializer = BookSerializer(book, data=data)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                    return Response({"error": "Book is not provided"}, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)

        return Response(serializer.data)

    def post(self, request, pk, format=None):
        book = self.get_object(pk)

        if not request.user.is_superuser:
            raise Http404

        if 'book' in request.data.keys():
            data = request.data['book']
            serializer = BookSerializer(book, data=data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Book is not provided"}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        book = self.get_object(pk)

        if not request.user.is_superuser:
            raise Http404

        try:
            book.delete()
            return Response({"message": "Book has been deleted."}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


