# Generated by Django 5.0.2 on 2024-03-14 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0008_alter_comment_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='musics.music_class'),
        ),
    ]
