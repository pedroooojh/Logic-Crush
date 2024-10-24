from django.db import models

from django.db import models

class Block(models.Model):
    TYPES = [
        ('VV', 'Verdadeiro/Verdadeiro'),
        ('VF', 'Verdadeiro/Falso'),
        ('FF', 'Falso/Falso'),
    ]
    block_type = models.CharField(max_length=2, choices=TYPES)

    def __str__(self):
        return self.block_type

