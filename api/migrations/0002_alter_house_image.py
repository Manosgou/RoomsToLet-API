# Generated by Django 4.0 on 2021-12-16 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]
