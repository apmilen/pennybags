# Generated by Django 2.2.3 on 2019-07-24 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20190629_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='bikability_score',
            new_name='bikeability_score',
        ),
    ]
