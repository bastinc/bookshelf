import pytest
from django.db import IntegrityError

from core.models.author import Author
from core.tests.factories.author import AuthorFactory


@pytest.mark.django_db
class TestAuthor:
    def test_author_creation_true(self):
        author = AuthorFactory(firstname="Georges R. R.", lastname="Martin")
        assert isinstance(author, Author)

    def test_author_creation_only_with_pseudonym_true(self):
        author = AuthorFactory(pseudonym="Richard Bachman")
        assert isinstance(author, Author)

    def test_duplicate_author_raise_integrity_error(self):
        with pytest.raises(IntegrityError):
            AuthorFactory.create_batch(2, firstname="Georges R. R.", lastname="Martin")

    def test_author_representation_true(self):
        author = AuthorFactory(firstname="Glen", lastname="Cook")
        assert str(author) == "Glen Cook"

    def test_author_representation_with_pseudonym_true(self):
        author = AuthorFactory(
            firstname="Pierre", lastname="Culliford", pseudonym="Peyo"
        )
        assert str(author) == "Peyo"
