# Generated by Django 3.1.6 on 2021-09-28 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20210928_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=9191919191, max_length=10),
        ),
    ]
