# Generated by Django 5.0.6 on 2024-08-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_alter_carinvetory_cars_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='km',
            field=models.FloatField(default=0, verbose_name='KM'),
            preserve_default=False,
        ),
    ]