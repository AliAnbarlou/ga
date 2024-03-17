# Generated by Django 5.0.2 on 2024-03-15 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_alter_artist_groups_alter_artist_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={},
        ),
        migrations.AlterModelManagers(
            name='artist',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='bio',
            new_name='biography',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='email',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='image',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='password',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='username',
        ),
        migrations.AddField(
            model_name='artist',
            name='name',
            field=models.CharField(default='Unknown Artist', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='picture',
            field=models.ImageField(default='default_picture.jpg', upload_to='artist_pictures/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]