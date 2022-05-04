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
                    "category_id"       : category.id,
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
        sort_by      = request.GET.get('sort_by', 'alphabetic_order')
        
        category_id  = request.GET.get('category_id', None)
        country_name = request.GET.get('country_name', None)
        label        = request.GET.get('label', None)
        
        offset       = int(request.GET.get('offset', 0))
        limit        = int(request.GET.get('limit', 12))
        
        sort_by_options = {
            "alphabetic_order" : "korean_name",
            "low_price"        : "price"
        }
        
        q = Q()
        
        if category_id:
            q &= Q(category__id = category_id)        
        
        if country_name:
            q &= Q(country_name = country_name)
            
        if label:
            q &= Q(label =label)
        
        products = Product.objects.filter(q).order_by(sort_by_options.get(sort_by, "alphabetic_order"))[offset:offset+limit]
            
        product_list = [{
            'sub_category_id': product.category.id,
            'product_id'     : product.id,
            'korean_name'    : product.korean_name,
            'english_name'   : product.english_name,
            'product_label'  : product.label,
            'country_name'   : product.country_name,   
            'product_weight' : product.weight,
            'product_price'  : product.price,
            'product_image'  : [image.image_url for image in product.image_set.all()]
        }for product in products]
        
        return JsonResponse({'product_list_data': product_list}, status=200)
        
        
class ProductDetailView(View):
    def get(self, request, product_id):
        
        if not Product.objects.filter(id = product_id).exists:
            return JsonResponse({'message' : 'DOES_NOT_EXIST'}, status = 400)
        
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
