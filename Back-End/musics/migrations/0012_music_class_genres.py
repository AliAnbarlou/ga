# Generated by Django 5.0.2 on 2024-03-15 07:44

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0011_remove_comment_approved'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='music_class',
            name='Genres',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
