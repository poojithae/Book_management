from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        feilds = fields = ['id', 'title', 'author', 'publication_date', 'isbn']
