from django.db import models


class Things(models.Model):
    name = models.CharField(
        unique=True,
        blank=False,
        max_length=30
    )
    description = models.CharField(
        unique=False,
        blank=True,
        max_length=120
    )
    quantity = models.IntegerField(
        blank=False,
        choices=[(x, x) for x in range(101)]
    )
