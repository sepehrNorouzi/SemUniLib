from django.http.response import Http404, JsonResponse
from django.db.models import Q

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import BookSerializer, FavoriteSerializer, ToReadSerializer
from .models import Book, Favorite, ToRead
import csv

class BooksView(APIView):

    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

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
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                    return Response({"error": "Book is not provided"}, status=status.HTTP_400_BAD_REQUEST)


class RecentBooks(APIView):

    def get(self, request, format=None):

        recentBooks = Book.objects.all().order_by('-published_date', '-rating', 'title')[:10]

        serializer = BookSerializer(recentBooks, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class BookDetail(APIView):

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk, format=None):
        book = self.get_object(pk)

        if not request.user.is_superuser:
            raise Http404

        if 'book' in request.data.keys():
            data = request.data['book']
            serializer = BookSerializer(book, data=data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
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



class FavoriteView(APIView): 
    
    def get(self, request, format=None):
        if not request.user.is_authenticated:
            raise Http404
        
        favorites = Favorite.objects.filter(Q(user=request.user.id))
        serializer = FavoriteSerializer(favorites, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        if not request.user.is_authenticated:
            raise Http404
        
        oldFav = Favorite.objects.filter(Q(book=request.data['book']) & Q(user=request.user))

        if len(oldFav) > 0:
            oldFav.delete()
            return Response({"message": "Favorite Already in the list"}, status=status.HTTP_208_ALREADY_REPORTED)

        favorite = Favorite()
        book = None
        try:
            book = Book.objects.get(pk=request.data['book'])
        except:
            raise Http404

        favorite.book = book
        favorite.user = request.user
        favorite.save()
        return Response(FavoriteSerializer(favorite).data, status=status.HTTP_201_CREATED)


def initDatabase(request):
    if(request.user.is_superuser):
        with open("../Server/books.csv", newline='', encoding='utf-8') as f:
            dataReader = csv.reader(f, delimiter=',', quotechar='"')
            next(dataReader)
            dataReader = list(dataReader)


            for i in range(120):
                isbn13 = 0
                if(dataReader[i][6] != ''):
                    isbn13 = str(int(float(dataReader[i][6])))
                authors = dataReader[i][7]
                publishedDate = int(float(dataReader[i][8]))
                title = dataReader[i][10]
                rating = float(dataReader[i][12])
                imageURL = dataReader[i][21]
                book = Book(title=title, author=authors, isbn13=isbn13, imageUrl=imageURL, rating=rating, published_date=publishedDate)
                try:
                    book.save()
                except:
                    continue 

        return JsonResponse({
            "message": "DONE"
        })


class ToReadView(APIView): 
    
    def get(self, request, format=None):
        if not request.user.is_authenticated:
            raise Http404
        
        toRead = ToRead.objects.filter(Q(user=request.user.id))
        serializer = ToReadSerializer(toRead, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        if not request.user.is_authenticated:
            raise Http404
        
        oldToread = ToRead.objects.filter(Q(book=request.data['book']) & Q(user=request.user))

        if len(oldToread) > 0:
            oldToread.delete()
            return Response({"message": "To Read Already in the list"}, status=status.HTTP_208_ALREADY_REPORTED)

        toRead = ToRead()
        book = None
        try:
            book = Book.objects.get(pk=request.data['book'])
        except:
            raise Http404

        toRead.book = book
        toRead.user = request.user
        toRead.save()
        return Response(ToReadSerializer(toRead).data, status=status.HTTP_201_CREATED)