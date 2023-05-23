# Generated by Django 4.1.3 on 2023-05-19 04:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_alter_blogs_post_on_alter_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='status',
            field=models.CharField(default='Approved', max_length=20),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='post_on',
            field=models.DateField(default=datetime.date(2023, 5, 19)),
        ),
    ]