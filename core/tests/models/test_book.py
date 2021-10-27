import pytest
from django.db import IntegrityError

from core.models.book import Book
from core.tests.factories.author import AuthorFactory
from core.tests.factories.book import BookFactory


@pytest.mark.django_db
class TestBook:
    @pytest.fixture
    def book(self):
        return BookFactory()

    def test_book_creation_true(self, book):
        assert isinstance(book, Book)

    def test_book_duplicate_raise_integrity_error(self):
        author = AuthorFactory(firstname="John", lastname="Doe")
        with pytest.raises(IntegrityError):
            BookFactory.create_batch(2, title="duplicate", author=author)

    def test_book_representation_true(self, book):
        assert str(book) == book.title
