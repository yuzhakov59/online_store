from django.db import models

class Category(models.Model):
    cat_name = models.CharField(max_length=150, verbose_name='название категории')
    cat_description = models.TextField(verbose_name='описание',blank=True, null=True)

    def __str__(self):
        return f'{self.cat_name} {self.cat_description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['cat_name']

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(verbose_name='описание',blank=True, null=True)
    picture = models.ImageField(upload_to='prod', verbose_name='фото продукта',blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    price = models.IntegerField(max_length=50, verbose_name='цена',blank=True, null=True)
    created_at = models.DateField(verbose_name='дата создания')
    updated_at = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
