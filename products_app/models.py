from django.db import models


class Assortment(models.Model):
    name = models.CharField(max_length=255, editable=False)
    measure_unit = models.CharField(max_length=5, editable=False)


class Division(models.Model):
    name = models.CharField(max_length=255, editable=False)
