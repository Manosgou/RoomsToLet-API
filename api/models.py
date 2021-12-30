import shortuuid
from django.db import models
from unidecode import unidecode
from django.shortcuts import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


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


class Request(models.Model):
    PENDING = 'PE'
    DONE = 'DO'
    STATUSES = [(PENDING, 'Pending'), (DONE, 'Done')]

    house = models.OneToOneField(House, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    status = models.CharField(
        max_length=2, choices=STATUSES, default=PENDING)

    def __str__(self) -> str:
        return f"Request for house:{self.house.title}"


class Booking(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=4)
    house = models.OneToOneField(House, on_delete=models.CASCADE)
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    duration = models.IntegerField(default=1, validators=[
        MaxValueValidator(50),
        MinValueValidator(1)
    ])

    def __str__(self) -> str:
        return f'The house: "{self.house.title}" has been booked by {self.lastname +" "+ self.firstname} with id: {self.id}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = shortuuid.ShortUUID().random(length=4).upper()
        super(Booking, self).save(*args, **kwargs)
