# Generated by Django 3.2.5 on 2021-10-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.PositiveIntegerField(default=100000),
        ),
    ]
