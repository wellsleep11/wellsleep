# Generated by Django 4.1.3 on 2023-05-02 03:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_blogs_post_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='post_on',
            field=models.DateField(default=datetime.date(2023, 5, 2)),
        ),
    ]
