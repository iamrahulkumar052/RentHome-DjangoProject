# Generated by Django 5.0.7 on 2024-08-01 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renter', '0004_homedetails_rid'),
    ]

    operations = [
        migrations.AddField(
            model_name='homedetails',
            name='people',
            field=models.IntegerField(default=1),
        ),
    ]
