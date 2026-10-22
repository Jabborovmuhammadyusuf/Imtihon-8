from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Author, Book

from .serialiser import AuthorSerialiser, BookSerialiser
from .permissions import CPermission

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all().prefetch_related('books')
    serializer_class = AuthorSerialiser
    permission_classes = [CPermission]

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerialiser
    permission_classes = [CPermission]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['price', 'published_year', 'pages']
