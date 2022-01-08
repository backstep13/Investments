from django.db import models


class Button(models.Model):
    title = models.CharField(max_length=200)
    interval = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    percent = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    addition = models.IntegerField(default=0)
    tax = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    def __str__(self):
        return self.title
