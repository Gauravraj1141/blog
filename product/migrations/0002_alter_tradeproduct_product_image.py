# Generated by Django 4.2.3 on 2023-07-20 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradeproduct',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/nyseimages'),
        ),
    ]
