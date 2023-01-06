from django.db import models
from setuptools._entry_points import _


# Create your models here.
class Thing(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    summary = models.TextField(default="Thats cool")
    price = models.DecimalField(decimal_places=2, max_digits=1000, default=0)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} , the price is {self.price}"


class Client(models.Model):
    name = models.CharField(max_length=200)
    address1 = models.CharField(_("address"), max_length=128)
    address2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64, default="Zanesville")
    zip_code = models.CharField(_("zip code"), max_length=5, default="43701")
    thing = models.ForeignKey(Thing,default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
