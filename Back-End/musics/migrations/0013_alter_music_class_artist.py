# Generated by Django 5.0.2 on 2024-03-15 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
        ('musics', '0012_music_class_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music_class',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artists.artist'),
        ),
    ]