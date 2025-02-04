from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Coupon(models.Model):
  code = models.CharField(max_length=50, unique=True)
  use_from = models.DateTimeField()
  use_to = models.DateTimeField()
  amount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)])
  active = models.BooleanField()

  def __str__(self):
    return self.code
