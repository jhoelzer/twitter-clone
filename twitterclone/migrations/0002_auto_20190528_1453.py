# Generated by Django 2.2.1 on 2019-05-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet',
            field=models.CharField(max_length=140),
        ),
    ]
