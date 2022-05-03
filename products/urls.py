from django.urls import path

from products.views import MenuView, CategoryView, SubCategoryView, ProductListView, ProductDetailView

urlpatterns = [
    path('/productlist', ProductListView.as_view()),
    path('/detail/<int:product_id>', ProductDetailView.as_view())
]