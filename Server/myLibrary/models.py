from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.TextField(blank=False, null=False)
    isbn13 = models.FloatField(null=False, blank=False, default=0)
    imageUrl = models.URLField(null=True, blank=True)
    rating = models.FloatField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.title} - {self.author}'

    class Meta: 
        ordering  = ('created_at',)

    