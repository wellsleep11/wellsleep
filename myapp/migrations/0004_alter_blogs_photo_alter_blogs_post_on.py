# Generated by Django 4.1.3 on 2023-03-09 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='photo',
            field=models.ImageField(upload_to='blogs/'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='post_on',
            field=models.CharField(max_length=20),
        ),
    ]
