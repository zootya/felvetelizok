from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Szak(models.Model):
    szakNev = models.CharField(max_length=50)
    tamogatott = models.BooleanField(default=True)
    def __str__(self):
        return self.szakNev
    class Meta:
        verbose_name_plural="Szak megnevezése"

class Felvetelizo(models.Model):
    nev = models.CharField(max_length=50)
    szul_evszam = models.IntegerField(
        validators=[
            MinValueValidator(1924),
            MaxValueValidator(2015)
        ]
    )
    pontszam = models.IntegerField()
    szak = models.ForeignKey("Szak", on_delete=models.CASCADE)
    def __str__(self):
        return self.nev
    class Meta:
        verbose_name_plural="Felveteliző neve"