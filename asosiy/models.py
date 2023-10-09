from django.db import models
from django.contrib.auth.models import AbstractUser


class Ombor(AbstractUser):
    nom = models.CharField(max_length=50)
    manzil = models.CharField(max_length=150)
    ism = models.CharField(max_length=150)

    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=150)
    narx = models.PositiveBigIntegerField()
    miqdor = models.CharField(max_length=50)
    olchov = models.CharField(max_length=10)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nom

class Mijoz(models.Model):
    nom = models.CharField(max_length=150)
    manzil = models.CharField(max_length=150)
    ism = models.CharField(max_length=150)
    tel = models.CharField(max_length=15)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    qarz = models.PositiveBigIntegerField()

    def __str__(self):
        return self.nom

