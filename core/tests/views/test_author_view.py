from rest_framework import status
from rest_framework.test import APITestCase

from core.tests.factories.author import AuthorFactory
from core.tests.factories.user import UserFactory


class TestAuthorView(APITestCase):
    def setUp(self) -> None:
        self.url = "/api/v1/authors"
        self.user = UserFactory()

    def test_get_authors_not_authenticated_401(self):
        response = self.client.get(path=self.url, format="json")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_authors_200(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(path=self.url, format="json")
        assert response.status_code == status.HTTP_200_OK

    def test_get_authors_count_2(self):
        AuthorFactory.create_batch(2)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(path=self.url, format="json")
        assert len(response.data) == 2

    def test_get_author_details(self):
        author = AuthorFactory(firstname="Jean", lastname="Dupont", pseudonym="jd")
        self.client.force_authenticate(user=self.user)
        path = "{}/{}".format(self.url, author.id)
        response = self.client.get(path=path, format="json")
        assert response.data == {
            "firstname": "Jean",
            "lastname": "Dupont",
            "pseudonym": "jd",
        }
