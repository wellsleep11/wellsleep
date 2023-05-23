# Generated by Django 4.1.3 on 2023-03-14 05:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_blogs_description_alter_blogs_post_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='category/')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.AlterField(
            model_name='blogs',
            name='post_on',
            field=models.DateField(default=datetime.date(2023, 3, 14)),
        ),
    ]