# Generated by Django 4.0 on 2022-01-03 15:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='thumbnails/')),
                ('rooms', models.IntegerField(default=1)),
                ('bathrooms', models.IntegerField(default=1)),
                ('has_kitchen', models.BooleanField(default=False)),
                ('has_AC', models.BooleanField(default=False)),
                ('has_parking', models.BooleanField(default=False)),
                ('has_wifi', models.BooleanField(default=False)),
                ('has_tv', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_available', models.BooleanField(default=True)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=200)),
                ('status', models.CharField(choices=[('PE', 'Pending'), ('DO', 'Done')], default='PE', max_length=2)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.house')),
            ],
        ),
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='house_images/')),
                ('house_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.house')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.CharField(editable=False, max_length=4, primary_key=True, serialize=False)),
                ('lastname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('duration', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('date', models.DateField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('house', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.house')),
            ],
        ),
    ]
