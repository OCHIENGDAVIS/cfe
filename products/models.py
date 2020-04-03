from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, default='title of the product')
    description = models.TextField(blank=True, null=True)
    summary = models.TextField(null=True)
    price = models.DecimalField(max_digits=100000, decimal_places=2, default=100.00)

    def __str__(self):
        return self.title
