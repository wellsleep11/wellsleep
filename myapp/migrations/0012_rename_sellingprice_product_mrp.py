# Generated by Django 4.1.3 on 2023-04-13 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_rename_photo1_product_image_rename_mrp_product_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sellingprice',
            new_name='mrp',
        ),
    ]