# Generated by Django 3.2.16 on 2023-02-01 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20230131_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.FloatField(),
        ),
    ]
