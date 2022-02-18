from rest_framework import serializers

from core.models.author import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "firstname",
            "lastname",
            "pseudonym",
        )
