from django.shortcuts import render
from django.http      import JsonResponse
from django.db.models import Q
from django.views     import View

from products.models import Product

class ProductListView(View):
    def get(self, request):        
        sub_category_id   = request.GET.get('sub_category', None)
        sort_by           = request.GET.get('sort_by', None)
        
        if sub_category_id:
                products = products.filter(sub_category_id = sub_category_id)
        
        sort_by_options = {
            "ascent"         : "korean_name",
            "low_price"      : "price"
        }
        
        q = Q()
        
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
                # 'image_info'     : [image.image_info for image in product.image_set.all()]
            }
        ]
        
        return JsonResponse({'product_detail_data': product_detail_list},status=200)
    
