from django.db import models
from django.conf import settings


class BookList(models.Model):
    name = models.CharField(max_length=100)
    public = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    books = models.ManyToManyField('books.Book')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
