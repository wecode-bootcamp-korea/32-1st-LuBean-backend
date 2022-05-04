from django.urls import path

from products.views import MainView, ProductListView, ProductDetailView

urlpatterns = [
    path('/main', MainView.as_view()),
    path('/list', ProductListView.as_view()),
    path('/detail/<int:product_id>', ProductDetailView.as_view())
]