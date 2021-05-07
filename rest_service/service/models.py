from django.db import models


class Data(models.Model):
    company = models.TextField(max_length=20)
    date = models.DateField()
    open = models.DecimalField(max_digits=20, decimal_places=6)
    high = models.DecimalField(max_digits=20, decimal_places=6)
    low = models.DecimalField(max_digits=20, decimal_places=6)
    close = models.DecimalField(max_digits=20, decimal_places=6)
    adj_close = models.DecimalField(max_digits=20, decimal_places=6)
    volume = models.IntegerField()

    def __str__(self):
        return self.company[:50] + " " + self.date.strftime("%Y-%m-%d")
