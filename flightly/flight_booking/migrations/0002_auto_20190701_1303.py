# Generated by Django 2.2.2 on 2019-07-01 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='Ticket Price'),
        ),
    ]