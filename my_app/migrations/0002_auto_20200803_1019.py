# Generated by Django 3.0.5 on 2020-08-03 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(max_length=200),
        ),
    ]
