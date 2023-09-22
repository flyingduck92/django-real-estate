from django.db import models


# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.DecimalField(max_digits=15, decimal_places=2)
    address = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.title
