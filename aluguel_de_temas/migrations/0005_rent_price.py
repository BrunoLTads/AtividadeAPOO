# Generated by Django 4.1.4 on 2023-07-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel_de_temas', '0004_alter_address_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
