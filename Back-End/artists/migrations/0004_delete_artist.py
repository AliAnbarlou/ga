# Generated by Django 5.0.2 on 2024-03-15 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_alter_artist_options_alter_artist_managers_and_more'),
        ('musics', '0015_remove_music_class_artist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Artist',
        ),
    ]
