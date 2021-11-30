from django.db import models
from .category import Category
from django.shortcuts import reverse

class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    second = models.BooleanField(default=False, null=False)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()

    @staticmethod
    def get_secondhand(status):
        if status:
            return Products.objects.filter(second=status)
        else:
            return Products.objects.filter(second=status)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"id": self.id})
