# Generated by Django 4.2.3 on 2023-07-17 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
