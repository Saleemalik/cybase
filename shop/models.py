from django.db import models
from django.db.models.query_utils import select_related_descend

# Create your models here.
COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)
SIZE_CHOICES = (
    ('L', 'Large'),
    ('M', 'Medium'),
    ('S', 'Small')
)

class Products(models.Model):

    productName = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.productName



class items(models.Model):
    product_name = models.ForeignKey(Products, on_delete=models.CASCADE)
    productColor = models.CharField(max_length=6, choices=COLOR_CHOICES, default='red')
    size = models.CharField(max_length=6, choices=SIZE_CHOICES, default='S')
    price = models.FloatField()

    def __str__(self):
        return self.productColor

    class Meta:
        unique_together = ('productColor', 'size', 'product_name')


