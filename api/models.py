from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_year = models.IntegerField()

    pages = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
