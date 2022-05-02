from django.urls import path

from products.views import MenuView, CategoryView, SubCategoryView, ProductListView

urlpatterns = [
    path('/menu', MenuView.as_view()),
    path('/category', CategoryView.as_view()),
    path('/subcategory', SubCategoryView.as_view()),
    path('/productlist', ProductListView.as_view())
]