from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Book(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    author = models.TextField(blank=False, null=False, default="")
    isbn13 = models.FloatField(null=False, blank=False, default=0)
    imageUrl = models.URLField(null=True, blank=True)
    rating = models.FloatField(blank=True, null=True)
    published_date = models.PositiveSmallIntegerField(blank=False, null=False, default=2000)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.title} - {self.author}'

    class Meta: 
        ordering  = ('created_at',)

    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    book = models.ForeignKey(Book, on_delete=CASCADE)


    def __str__(self) -> str:
        return f'{self.user.username} - {self.id}'


class ToRead(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    book = models.ForeignKey(Book, on_delete=CASCADE)


    def __str__(self) -> str:
        return f'{self.user.username} - {self.id}'