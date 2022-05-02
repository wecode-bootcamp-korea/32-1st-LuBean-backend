from django.shortcuts import render
from django.http      import JsonResponse
from django.views     import View

from products.models import Menu, Category, Product

class MenuView(View):
    def get(self, request):
        menus = Menu.objects.all()
        # categories = Category.objects.all()
        
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
        products = Product.objects.all()
        
        sub_category_id   = request.GET.get('sub_category', None)
        ascent            = request.GET.get('ascent', None)
        low_price         = request.GET.get('low_price', 0)
        
        sort_by = request.GET.get('sort_by', None)
        
        sort_by_options = {
            "sub_category"   : "sub_category_id",
            "ascent"         : "korean_name",
            "low_price"      : "price"
        }
            
        product_list = [{
            'product_id'     : product.id,
            'product_name'   : product.name,
            'product_label'  : product.label,
            'country_name'   : product.country_name,
            'product_weight' : product.weight,
            'product_price'  : product.price,
            'product_image'  : [image.image_url for image in product.image]
        }for product in products]
        
        return JsonResponse({'product_list_data': product_list}, status=200)
        