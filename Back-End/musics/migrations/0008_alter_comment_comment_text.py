# Generated by Django 5.0.2 on 2024-03-14 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(max_length=3000),
        ),
    ]
