from rest_framework import viewsets

from core.models.author import Author
from core.serializers.author import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        return Author.objects.all()
