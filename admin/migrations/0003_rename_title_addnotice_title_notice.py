# Generated by Django 3.2.7 on 2021-09-22 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_addnotice_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addnotice',
            old_name='title',
            new_name='title_notice',
        ),
    ]
