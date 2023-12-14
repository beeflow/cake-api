"""copyright (c) 2014 - 2023 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

YUM_FACTOR_MIN = 1
YUM_FACTOR_MAX = 5


class Cake(models.Model):
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=200)
    image_url = models.URLField(max_length=2048)
    yum_factor = models.IntegerField(
        validators=[
            MinValueValidator(YUM_FACTOR_MIN),
            MaxValueValidator(YUM_FACTOR_MAX),
        ]
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(yum_factor__gte=YUM_FACTOR_MIN) & models.Q(yum_factor__lte=YUM_FACTOR_MAX),
                name="A yum_factor value is valid between 1 and 5",
            )
        ]
