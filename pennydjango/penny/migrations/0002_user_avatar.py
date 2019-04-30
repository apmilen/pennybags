# Generated by Django 2.2 on 2019-04-26 19:12

from django.db import migrations, models
import penny.utils


class Migration(migrations.Migration):

    dependencies = [
        ('penny', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=penny.utils.avatar_path, validators=[penny.utils.validate_file_size]),
        ),
    ]