from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add test product to the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(cat_name='Хлеб', cat_description='Хлебобулочные')

        products = [
            {'name': 'Белый', 'category': category,'created_at': '1901-01-01','updated_at': '1901-01-01'},
            {'name': 'Черный', 'category': category,'created_at': '1901-01-01','updated_at': '1901-01-01'},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))