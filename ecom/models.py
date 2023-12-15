
from django.db import models
from django.urls import reverse



class Category(models.Model):
   category_name=models.CharField(max_length=70)
   slug=models.SlugField(max_length=100,unique=True)
   description=models.TextField(max_length=500)
   cat_image=models.ImageField(upload_to='photos/categories')

   def get_url(self):
     return reverse('products_by_category', args=[self.slug])
   
   def __str__(self):
      return self.category_name
   

class Products(models.Model):
   product_name=models.CharField(max_length=200)
   description=models.TextField(max_length=500)
   price=models.DecimalField(max_digits=7,decimal_places=2)
   images=models.ImageField(upload_to='photos/products')
   stock=models.IntegerField()
   is_available=models.BooleanField(default=True)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   slug = models.SlugField(default='')

   
   #def get_url(self):
     #return reverse('product_detail', args=[self.category.slug, self.slug])   
   
   def get_url(self):
        if self.category and self.slug:
            return reverse('product_detail', args=[self.category.slug, self.slug])
        return '#'
   def __str__(self):
      return self.product_name
   

 
     
   
   

# Create your models here.