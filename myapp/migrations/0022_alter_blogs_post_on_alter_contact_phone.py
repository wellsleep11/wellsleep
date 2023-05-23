# Generated by Django 4.1.3 on 2023-05-12 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_alter_blogs_post_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='post_on',
            field=models.DateField(default=datetime.date(2023, 5, 12)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]