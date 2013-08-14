from django.db import models
from django.conf import settings

class Author(models.Model):

    # This model is very simple and naive on purpose at the moment
    # It needs to deal with multiple authors with the same name
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    display_name = models.CharField(max_length=310, blank=True, help_text="The way the author's name is normally displayed.  Defaults to first_name last_name.")
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    active = models.BooleanField(default=True, blank=True)

    class Meta:
        ordering = ['-last_name', '-first_name']

    def __unicode__(self):
        return u'{0}, {1}'.format(self.last_name, self.first_name)

    def save(self, *args, **kwargs):
        if not self.display_name:
            self.display_name = u'{0} {1}'.format(self.first_name, self.last_name)
        super(Author, self).save(*args, **kwargs)


class Book(models.Model):
    # A lot of things are currently being ignored for simplicity
    # publisher, date published, editions, etc.  Just keeping it simple for now
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField('Author')
    isbn = models.CharField(max_length=13, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    class Meta:
        ordering = ['-title']

    def __unicode__(self):
        return u'{0}'.format(self.title)
