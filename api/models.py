from django.db import models
from unidecode import unidecode
from PIL import Image
from django.shortcuts import reverse
from django.utils.text import slugify


# Create your models here.

class House(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(default='', blank=True)
    rooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    has_kitchen = models.BooleanField(default=False)
    has_AC = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    has_tv = models.BooleanField(default=False)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(House, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('house', kwargs={"slug": self.slug})


class HouseImage(models.Model):
    house_id = models.ForeignKey(House, default='', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="houses/")


class Requests(models.Model):
    PENDING = 'PE'
    DONE = 'DO'
    STATUSES = [(PENDING, 'Pending'), (DONE, 'Done')]

    house = models.OneToOneField(House, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    status = models.CharField(
        max_length=2, choices=STATUSES, default=PENDING)
