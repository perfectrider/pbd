from django.db import models


class Assortment(models.Model):
    name = models.CharField(max_length=255)
    measure_unit = models.CharField(max_length=5)


class Division(models.Model):
    name = models.CharField(max_length=255)
