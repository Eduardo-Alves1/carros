# Generated by Django 5.0.6 on 2024-08-08 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carinvetory',
            name='cars_count',
            field=models.IntegerField(verbose_name='Carros em Estoque'),
        ),
        migrations.AlterField(
            model_name='carinvetory',
            name='cars_value',
            field=models.FloatField(verbose_name='Valor Total em do Estoque'),
        ),
    ]
