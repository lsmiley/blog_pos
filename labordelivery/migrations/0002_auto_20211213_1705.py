# Generated by Django 3.0.7 on 2021-12-13 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labordelivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labordelivery',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
