# Generated by Django 2.2.7 on 2020-02-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0019_auto_20200214_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='databaseinformation',
            name='like',
        ),
        migrations.AddField(
            model_name='databaseinformation',
            name='rating',
            field=models.IntegerField(default=3),
        ),
    ]