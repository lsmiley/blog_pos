# Generated by Django 3.2.5 on 2021-12-15 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labordeliverytype', '0002_auto_20211213_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labordeliverytype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
