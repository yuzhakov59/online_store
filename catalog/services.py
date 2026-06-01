from catalog.models import Product, Category
from config.settings import CACHE_ENABLED
from django.core.cache import cache


def get_catalog_from_cache():
    """Проверяем режим кеширование, наличие данных в кеше
    выдает из кеша, при отсутствие данных в кеше делает запрос в базу"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    catalog = cache.get(key)
    if catalog is not None:
        return catalog
    catalog = Product.objects.all()
    cache.set(key, catalog)
    return catalog


def get_products_by_category(category_id):
    """
    Получает список продуктов для указанной категории, используя кеширование.
    """
    cache_key = f'products_category_{category_id}'
    products = cache.get(cache_key)

    if products is None:
        try:
            category = Category.objects.get(pk=category_id)
            products = Product.objects.filter(category=category)
            cache.set(cache_key, products, timeout=60*15)  # Кешируем на 15 минут
        except Category.DoesNotExist:
            products = Product.objects.none()
    return products