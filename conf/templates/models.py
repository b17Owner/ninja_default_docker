# from django.db import models
# # from django.utils import timezone
# # from django.contrib.auth.models import User


# class Category(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     slug = models.SlugField(
#         verbose_name=('url'),
#         blank=False,
#         unique=True,
#     )
#     name = models.CharField(
#         max_length=100
#     )
#     description = models.TextField(
#         blank=True,
#         verbose_name="Описание")
#     img = models.ImageField(
#         blank=True,
#         verbose_name="Ссылка на картинку")
#     parent_category = models.ForeignKey(
#         'self',
#         on_delete=models.SET_NULL,
#         related_name='child_category_list',
#         verbose_name=('Родительская категория'),
#         blank=True,
#         null=True
#     )

#     def __str__(self):
#         return self.name


# class Product(models.Model):
#     # AVAIL = True
#     # NOTAVAIL = False
#     # AVAIL_PRODUCT_CHOICES = [
#     #     (AVAIL, 'Товар в наличии'),
#     #     (NOTAVAIL, 'Товар отсутствует')
#     # ]
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     name = models.CharField(
#         max_length=256,
#         verbose_name="Название",
#         unique=True)
#     description = models.TextField(
#         blank=True,
#         verbose_name="Описание")
#     price = models.PositiveIntegerField(
#         verbose_name="Цена",
#         default=0)
#     price_discount = models.PositiveIntegerField(
#         verbose_name="Цена со скидкой",
#         default=0)
#     img = models.ImageField(
#         null=True,
#         blank=True,
#         verbose_name="Ссылка на картинку")
#     avail = models.BooleanField(
#         # choices=AVAIL_PRODUCT_CHOICES,
#         default=False,
#         verbose_name="Наличие товара")
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.SET_NULL,
#         null=True,
#         verbose_name="Категория")

#     def __str__(self):
#         return self.name


# class SpecificationCategory(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     name = models.CharField(max_length=256, verbose_name="Название",
#                             unique=True)

#     def __str__(self):
#         return self.name


# class Unit(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     name = models.CharField(max_length=50, unique=True)

#     def __str__(self):
#         return self.name


# class Specification(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     category = models.ForeignKey(
#         SpecificationCategory,
#         on_delete=models.CASCADE,
#         null=True,
#         verbose_name="Характеристика")
#     value = models.CharField(max_length=100, verbose_name="Значение",
#                              unique=True)
#     unit = models.ForeignKey(Unit, verbose_name="Ед.измерения",
#                              null=True, on_delete=models.SET_NULL, blank=True)
#     active = models.BooleanField(default=True, verbose_name="Активно")
#     products = models.ManyToManyField(Product, through='ProductSpecifications')

#     def __str__(self):
#         return self.category.name + ' ' + self.value


# class ProductSpecifications(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
#     unique_together = [['product', 'specification']]
