# Generated by Django 5.0.6 on 2024-07-10 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_carinvetory_alter_car_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
