from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    pseudonym = models.CharField(max_length=255, blank=True, null=True, unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["firstname", "lastname"], name="unique_name"
            )
        ]

    def __str__(self):
        if self.pseudonym and len(self.pseudonym) > 0:
            return f"{self.pseudonym}"
        return f"{self.firstname} {self.lastname}"
