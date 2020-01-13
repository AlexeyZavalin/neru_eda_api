from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=64,
                             verbose_name='Наименование категории')
    image = models.ImageField(max_length=100, upload_to='media/categories')

    def __str__(self):
        return self.title


class Establishment(models.Model):
    name = models.CharField(max_length=128,
                            verbose_name='Наименование заведения')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    logo = models.ImageField(max_length=100,
                             upload_to='media/logos',
                             height_field=400,
                             width_field=400,
                             verbose_name='Логотип заведения')
    image = models.ImageField(max_length=100,
                              upload_to='media/establishments',
                              height_field=1000,
                              width_field=1000,
                              verbose_name='Фото заведения')
    popular = models.BooleanField(default=False,
                                  verbose_name='Популярное заведение')

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='Наименование категории в меню заведения')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=64, verbose_name='Наименование товара')
    price = models.DecimalField(decimal_places=2,
                                max_digits=9,
                                verbose_name='Цена товара')
    establishment = models.ForeignKey(Establishment,
                                      on_delete=models.CASCADE,
                                      verbose_name='Заведение')
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)
    ingredients = models.TextField(max_length=256,
                                   null=True,
                                   blank=True,
                                   verbose_name='Ингредиенты')
    popular = models.BooleanField(default=False,
                                  verbose_name='Популярный товар')

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(max_length=100,
                              upload_to='media/products',
                              height_field=1000,
                              width_field=1000)


class Kitchen(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    PAYMENT_TYPES = [('OL', 'Оплата онлайн'),
                     ('CS', 'Оплата наличными, при получении'),
                     ('CA', 'Оплата картой, при получении')]
    payment_type = models.CharField(max_length=2,
                                    choices=PAYMENT_TYPES,
                                    unique=True)

    def __str__(self):
        return self.payment_type


class EstablishmentPayments(models.Model):
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('establishment', 'payment_type'), )
