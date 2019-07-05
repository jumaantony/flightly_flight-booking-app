# Generated by Django 2.2.3 on 2019-07-04 19:01

from django.db import migrations, models
import django_cryptography.fields
import flightly.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190701_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightlyuser',
            name='photograph',
            field=django_cryptography.fields.encrypt(models.ImageField(
                default='img/62751906-b389-4663-97c6-ccf8b1f744eb_f5laht', upload_to=flightly.users.models.user_directory_path, verbose_name='Passport Photograph')),
        ),
    ]
