# Generated by Django 4.1.3 on 2023-05-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_blogs_status_alter_blogs_post_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('approved', 'approved')], default='Approved', max_length=20),
        ),
    ]