# Generated by Django 2.2.24 on 2021-10-26 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(blank=True, max_length=255, null=True)),
                ("lastname", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "pseudonym",
                    models.CharField(
                        blank=True, max_length=255, null=True, unique=True
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="author",
            constraint=models.UniqueConstraint(
                fields=("firstname", "lastname"), name="unique_name"
            ),
        ),
    ]
