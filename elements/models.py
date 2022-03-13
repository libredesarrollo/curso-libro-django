from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Type(models.Model):
    title = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Element(models.Model):
    title = models.CharField(max_length=255)
    url_clean = models.SlugField(max_length=255,blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2, default=6.10) # 12345678.10
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)