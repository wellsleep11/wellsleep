# Generated by Django 4.1.3 on 2023-05-04 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='userid',
        ),
    ]
