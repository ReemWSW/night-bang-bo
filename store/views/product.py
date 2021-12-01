from django.shortcuts import get_object_or_404, render
from store.models.category import Category
from store.models.product import Products


def product_detail_view(request, id):
    categories = Category.get_all_categories()
    product = Products.objects.filter(id=id)
    context = {
        "categories":categories,
        "products":product
    }
    print(product)
    return render(request, "product.html", context)
