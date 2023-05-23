# Generated by Django 4.1.3 on 2023-03-02 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mrp', models.FloatField()),
                ('sellingprice', models.FloatField()),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='product/')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]