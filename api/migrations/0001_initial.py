# Generated by Django 3.2.5 on 2021-11-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
                ('numworkstation', models.IntegerField(db_column='Numworkstation', default='0')),
                ('numserver', models.IntegerField(db_column='Numserver', default='0')),
                ('addlconsole', models.IntegerField(db_column='addlconsole', default='0')),
                ('productcomplexitybase', models.FloatField(db_column='ProductComplexityBase', default='550')),
                ('productcomplexityfac', models.FloatField(db_column='ProductComplexityFac', default='1.0')),
            ],
        ),
    ]