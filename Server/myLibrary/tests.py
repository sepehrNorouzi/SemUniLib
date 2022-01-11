from django.http import response
from django.test import TestCase
import rest_framework
from .models import Book, Favorite
from django.contrib.auth.models import User
from django.contrib.auth import login
import csv, json


def initDummy():
    
    with open("../Server/books.csv", newline='', encoding='utf-8') as f:
        dataReader = csv.reader(f, delimiter=',', quotechar='"')
        next(dataReader)
        dataReader = list(dataReader)
        for i in range(20):
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

class BasicTest(TestCase):
    def test_fields(self):
        book = Book()
        book.title = "The test"
        book.isbn13 = 1234567890111
        book.author = "Me Myself And I"
        book.imageUrl = "https://st.depositphotos.com/1741875/1237/i/600/depositphotos_12376816-stock-photo-stack-of-old-books.jpg"
        book.published_date = 2021
        book.rating = 5
        book.save()


        record = Book.objects.get(pk=1)

        self.assertEqual(record, book, "Fields are ok")


    def test_favorites(self):
        _user = User()

        _user.username = "Test"
        _user.password = "123456789abcdefghi"

        _user.save()

        book = Book()
        book.title = "The test"
        book.isbn13 = 1234567890111
        book.author = "Me Myself And I"
        book.imageUrl = "https://st.depositphotos.com/1741875/1237/i/600/depositphotos_12376816-stock-photo-stack-of-old-books.jpg"
        book.published_date = 2021
        book.rating = 5
        book.save()

        favorite = Favorite()
        favorite.user = User.objects.get(pk=1)
        favorite.book = Book.objects.get(pk=1)

        favorite.save()

        record = Favorite.objects.get(pk=1)

        self.assertEqual(favorite, record, "Favorite Test Done")


    def test_view_get_books(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_view_get_book(self):
        book = Book()
        book.title = "The test"
        book.isbn13 = 1234567890111
        book.author = "Me Myself And I"
        book.imageUrl = "https://st.depositphotos.com/1741875/1237/i/600/depositphotos_12376816-stock-photo-stack-of-old-books.jpg"
        book.published_date = 2021
        book.rating = 5
        book.save()


        response = self.client.get('/books/1/')
        self.assertEqual(response.status_code, 200)

    def test_recent_books(self):
        initDummy()

        response = self.client.get('/books/recents/')
        self.assertEqual(response.status_code, 200)


    def test_favorites_without_login(self):
        _user = User()

        _user.username = "Test"
        _user.password = "123456789abcdefghi"

        _user.save()

        book = Book()
        book.title = "The test"
        book.isbn13 = 1234567890111
        book.author = "Me Myself And I"
        book.imageUrl = "https://st.depositphotos.com/1741875/1237/i/600/depositphotos_12376816-stock-photo-stack-of-old-books.jpg"
        book.published_date = 2021
        book.rating = 5
        book.save()


        favorite = Favorite()
        favorite.user = User.objects.get(pk=1)
        favorite.book = Book.objects.get(pk=1)

        favorite.save()

        response = self.client.get('/books/favorites/')

        self.assertEqual(response.status_code, 404)

    