# Generated by Django 3.1 on 2020-08-27 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_auto_20200827_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='klik op de link om post te lezen', max_length=255),
        ),
    ]
