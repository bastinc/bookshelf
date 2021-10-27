from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "author"], name="unique_title_by_author"
            )
        ]

    def __str__(self):
        return self.title
