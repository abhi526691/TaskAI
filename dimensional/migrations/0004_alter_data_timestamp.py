# Generated by Django 3.2.7 on 2022-01-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dimensional', '0003_alter_data_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='timestamp',
            field=models.DateField(),
        ),
    ]
