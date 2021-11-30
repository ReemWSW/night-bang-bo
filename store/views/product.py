from django.shortcuts import get_object_or_404, render
from store.models.product import Products


def product_detail_view(request, id):
    product = Products.objects.filter(id=id)
    print(product)
    return render(request, "product.html", {"products":product})
