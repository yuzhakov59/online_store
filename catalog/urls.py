from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ProductDetailView, contacts, ProductListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryProductListView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog_list'),
    path('catalog/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('catalog/create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('catalog/contacts/', contacts, name='contacts'),
    path('catalog/category/<int:category_id>/', CategoryProductListView.as_view(), name='category_product_list'),
]