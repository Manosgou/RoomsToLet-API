# Generated by Django 4.0 on 2021-12-31 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_booking_total_pice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='total_pice',
            new_name='total_price',
        ),
    ]