# Generated by Django 4.1.7 on 2023-03-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("handleMovies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movieslist",
            name="poster_url",
            field=models.CharField(
                default="https://i.etsystatic.com/33462116/r/il/174294/4425593935/il_1080xN.4425593935_j2d4.jpg",
                max_length=1000,
            ),
        ),
    ]
