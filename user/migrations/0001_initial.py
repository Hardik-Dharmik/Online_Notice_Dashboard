# Generated by Django 3.2.5 on 2021-09-15 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Of_Birth', models.DateField()),
                ('Roll_No', models.IntegerField(unique=True)),
                ('Department', models.CharField(max_length=100)),
                ('Year_Of_Study', models.CharField(max_length=4)),
                ('Gender', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
