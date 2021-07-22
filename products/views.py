from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Products
from products.forms import ProductForm

def main_page_view(request):
    products = Products.objects.all()
    print(products)
    for i in products:
        print('id:', i.id)
        print('title:', i.title)
        print('price:', i.price)
        print()
    data = {
        'title': 'Главная страница',
        'product_list': products
    }
    return render(request, 'index.html', context=data)


def product_item_view(request, product_id):
    product = Products.objects.get(id=product_id)
    data = {
        'product': product,
        'title': product.title,
    }
    return render(request, 'item.html', context=data)


def add_product(request):
    if request.method == 'GET':

        data={
            'form':ProductForm()

        }
        return render(request,'add.html',context=data)
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')