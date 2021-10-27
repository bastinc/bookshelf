import factory

from core.models.book import Book
from core.tests.factories.author import AuthorFactory


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Sequence(lambda n: "title_{:05d}".format(n))
    author = factory.SubFactory(AuthorFactory)
