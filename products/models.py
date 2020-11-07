from django.db import models

# Create your models here.


# Category Model
class Category(models.Model):

    # verbose name metaclass
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # return the name
    def __str__(self):
        return self.name

    # return the friendly name if we want
    def get_friendly_name(self):
        return self.friendly_name


# Products Model
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    # stock-keeping unit or SKU is a unique identifier for 
    # each distinct product and service that can be purchased.
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # string method will just return the products name
    def __str__(self):
        return self.name
