from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    is_active = models.BooleanField(verbose_name='Активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название', max_length=200, unique=True)
    short_desc = models.CharField(verbose_name='Краткое описание продукта', max_length=100, blank=True)
    description = models.TextField(verbose_name='Описание продукта', blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(upload_to='products_images', blank=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе', default=0)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"
