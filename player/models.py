from django.db import models
from decimal import Decimal

# Create your models here.
class PlayerRun(models.Model):
    date = models.DateField(auto_now=True)
    distance = models.DecimalField(decimal_places=2, max_digits=99)
    time = models.DecimalField(decimal_places=2, max_digits=99)
    mass = models.DecimalField(decimal_places=2, max_digits=99)

    @property
    def kph(self):
        hours = self.time / 60
        return Decimal(self.distance / hours)

    @property
    def calories(self):
        vo2 = (Decimal(2.209) + Decimal(3.1633)) * self.kph
        return (Decimal(4.86) * self.mass * vo2) / 1000
