import pytest

from core.serializers.author import AuthorSerializer
from core.tests.factories.author import AuthorFactory


@pytest.mark.django_db
class TestAuthorSerializer:
    @pytest.fixture
    def author(self):
        return AuthorFactory()

    def test_author_serializer_fields(self, author):
        serializer = AuthorSerializer(instance=author)
        assert list(serializer.fields.keys()) == ["firstname", "lastname", "pseudonym"]
