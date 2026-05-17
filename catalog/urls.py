from django.urls import path


from .views import catalog_list, prod_detail, contacts

app_name = 'catalog'

urlpatterns = [
    path('', catalog_list, name='catalog_list'),
    path('prod_detail/<str:prod_name>/', prod_detail, name='prod_detail'),
    path('contacts/', contacts, name='contacts'),
]