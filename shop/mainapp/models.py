from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()


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
    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title


class Notebook(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display_type = models.CharField(max_length=255, verbose_name='Тип дисплея')
    processor_freq = models.CharField(max_length=255, verbose_name='Частота процессора')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    video = models.CharField(max_length=255, verbose_name='Видеокарта')
    time_without_charge = models.CharField(max_length=255, verbose_name='Время работы аккумуляторы')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Phone(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display_type = models.CharField(max_length=255, verbose_name='Тип дисплея')
    resolution = models.CharField(max_length=255, verbose_name='Разрешение')
    accum_volume = models.CharField(max_length=255, verbose_name='Емкость Аккумулятора')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    sd = models.BooleanField(default=True)
    sd_volume_max = models.CharField(max_length=255, verbose_name='Максимальный объем встроенной памяти')
    main_cam_mp = models.CharField(max_length=255, verbose_name='Основная камера')
    front_cam_mp = models.CharField(max_length=255, verbose_name='Фронтальная камера')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Beer(Product):
    Percent_Alcohol = models.CharField(max_length=255, verbose_name='Процент Алкоголя')
    Bitterness_Unit = models.CharField(max_length=255, verbose_name='Горечь')
    Color_Beer = models.CharField(max_length=255, verbose_name='Цвет Пиво')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Portraits(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    portraits_type = models.CharField(max_length=255, verbose_name='Тип Портрета')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Underpants(Product):
    size = models.CharField(max_length=255, verbose_name='Размер')
    presence_drawing = models.BooleanField(default=True)
    drawing = models.ImageField(verbose_name='Изображение')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Socks(Product):
    size = models.CharField(max_length=255, verbose_name='Размер')
    presence_text = models.BooleanField(default=True)
    drawing = models.ImageField(verbose_name='Изображение')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Hats(Product):
    size = models.CharField(max_length=255, verbose_name='Размер')
    hats_type = models.CharField(max_length=255, verbose_name='Тип Портрета')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    finals_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая Цена')

    def __str__(self):
        return "Продукт: {}(для корзины)".format(self.product.title)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_product = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая Цена')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=28, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)
