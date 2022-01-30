from django.db import models
from django.contrib.auth.models import User


class Investor(models.Model):
    investor = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    account = models.PositiveIntegerField(default=0)
    total_invest = models.PositiveIntegerField(default=0)
    profit = models.PositiveIntegerField(default=0)


class Investment(models.Model):
    KIND = (
        ('deposit', 'Deposit'),
        ('bond', 'Bond'),
        ('found', 'Found'),
    )

    investor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    i_type = models.CharField(max_length=100, choices=KIND, default='deposit')
    interval = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    percent = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    def save(self, *args, **kwargs):
        acc = Investor.objects.get(investor=self.investor)
        if acc.account >= self.amount:
            acc.account -= self.amount
            acc.total_invest += self.amount
            acc.save()
            super().save(*args, **kwargs)  # Call the "real" save() method.
