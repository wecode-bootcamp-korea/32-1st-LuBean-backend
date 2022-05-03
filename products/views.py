from django.shortcuts import render
from django.http      import JsonResponse
from django.db.models import Q
from django.views     import View

from products.models import Product, Menu, Category

class MenuView(View):
    def get(self, request):
        menus = Menu.objects.all()
        
        menu_list = [
            {
                "menu_id"   : menu.id,
                "menu_name" : menu.name,
                "category_list" : [{
                    "category_id" : category.id,
                    "category_name"     : category.name,
                    "sub_category_name" : category.sub_category
                } for category in menu.category_set.all()]
            } for menu in menus
        ]
        
        return JsonResponse({"result" : menu_list}, status = 200)

    
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        
        category_list = [
            {
                "category_id"   : category.id,
                "category_name" : category.name
            } for category in categories
        ]
        
        return JsonResponse({"result" : category_list}, status = 200)


class SubCategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        
        sub_category_list = [
            {
                "category_id"       : category.id,
                "sub_category_name" : category.sub_category,
                "sub_detail"        : category.sub_detail
            } for category in categories
        ]
        
        return JsonResponse({"result" : sub_category_list}, status = 200)

    
class ProductListView(View):
    def get(self, request):
        sub_category_id   = request.GET.get('sub_category', None)
        sort_by           = request.GET.get('sort_by', None)
        country_name      = request.GET.get('country_name', None)
        
        if sub_category_id:
            products = products.filter(sub_category_id = sub_category_id)
        
        sort_by_options = {
            "ascent"         : "korean_name",
            "low_price"      : "price"
        }
        
        q = Q()
        
        if country_name:
            q &= Q(product_country_name = country_name)
            
        products = Product.objects.filter(q).order_by(sort_by_options.get(sort_by))
            
        product_list = [{
            'product_id'     : product.id,
            'product_name'   : product.name,
            'product_label'  : product.label,
            'country_name'   : product.country_name,   
            'product_weight' : product.weight,
            'product_price'  : product.price,
            'product_image'  : [image.image_url for image in product.image_set.all()]
        }for product in products]
        
        return JsonResponse({'product_list_data': product_list}, status=200)


# class CountryListView(View):
#     def get(self, request):
#         products = Product.objects.all()

#         country_list = [
#             {
                
#             }
#         ]
        
class ProductDetailView(View):
    def get(self, request, product_id):
        if not Product.objects.filter(id = product_id).exists:
            return JsonResponse({'message' : 'DOES_NOT_EXIST'}, status = 401)
        
        product = Product.objects.get(id = product_id)
        
        product_detail_list = [
            {
                'product_id'     : product.id,
                'korean_name'    : product.korean_name,
                'english_name'   : product.english_name,
                'product_weight' : product.weight,
                'product_detail' : product.detail,
                'image_url'      : [image.image_url for image in product.image_set.all()],
                'image_info'     : [image.image_info for image in product.image_set.all()]
            }
        ]
        
        return JsonResponse({'product_detail_data': product_detail_list},status=200)
    
