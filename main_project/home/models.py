from django.db import models
from django.urls import reverse

# Create your models here.
class Caterogy(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='categories', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('category_list', args=[self.slug])
    

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Caterogy, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subcategories', blank=True, null=True)

    


    class Meta:
        ordering = ['name']
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='products',  blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name