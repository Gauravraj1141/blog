# Generated by Django 4.2.3 on 2023-07-20 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_tradeproduct_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradeproduct',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='nyseimages'),
        ),
    ]