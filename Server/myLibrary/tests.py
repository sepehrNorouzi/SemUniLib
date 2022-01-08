from django.test import TestCase
from .models import Book, Favorite
from django.contrib.auth.models import User


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