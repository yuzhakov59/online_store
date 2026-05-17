from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def catalog_list(request):
    cata_prod = Product.objects.all()
    context = {"cata_prod": cata_prod}
    return render(request, 'catalog_list.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse("Данные отправлены!")
    return render(request,'contacts.html' )


def prod_detail(request, prod_name):
    product = get_object_or_404(Product, name=prod_name)
    context = {"product": product}
    return render(request, 'prod_detail.html', context)