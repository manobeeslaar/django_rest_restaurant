from django.db import models

# Create your models here.
#menu items
class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='menu/images', default='menu/images/default.png')
    category = models.CharField(max_length=30, default='')

    def __str__(self):
        return f'{self.name} - {self.category} - ${self.price}'