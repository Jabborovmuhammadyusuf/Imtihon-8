from rest_framework import serializers

from .models import Author, Book

class BookShortSerialiser(serializers.ModelSerializer):
    class Meta:

        model = Book
        fields = ['id', 'title', 'price']

class AuthorSerialiser(serializers.ModelSerializer):

    books = BookShortSerialiser(many=True, read_only=True,)

    class Meta:
        model = Author
        fields = '__all__'

class BookSerialiser(serializers.ModelSerializer):


    class Meta:
        model = Book
        fields = '__all__'
