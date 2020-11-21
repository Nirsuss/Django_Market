from django.db import models


# ***************
# 1 Категории
# 2 Продукт
# 3 Сохранение покупок
# 4 Корзина
# 5 Заказ
# ****************
# _____________
# 6 Покупатель
# 7 Хар-ки товара
# _____________


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя Категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title
 