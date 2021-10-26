import factory

from core.models.author import Author


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author
