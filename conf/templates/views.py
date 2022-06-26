# from typing import List
# from ninja import NinjaAPI
# from . import models, schemas


# api = NinjaAPI()


# @api.get('/category', response=List[schemas.Category])
# def get_category(request):
#     return models.Category.objects.all()


# @api.get('/products', response=List[schemas.Product])
# def get_products(request, category_id: int):
#     return models.Product.objects.all().filter(category_id=category_id)


# @api.get('/product', response=schemas.Product)
# def get_product(request, id: int):
#     return models.Product.objects.get(pk=id)
