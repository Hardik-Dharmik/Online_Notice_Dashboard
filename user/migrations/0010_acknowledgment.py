# Generated by Django 3.2.5 on 2021-09-23 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_addnotice_year'),
        ('user', '0009_profile_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acknowledgment',
            fields=[
                ('ack_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_acknowledged', models.BooleanField(default=False)),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.addnotice')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
    ]