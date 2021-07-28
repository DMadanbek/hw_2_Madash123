from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Products
from products.forms import ProductForm,RegisterForm

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

@login_required(login_url='/login/')
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


from .forms import LoginForm

def logout(request):
    auth.logout(request)
    return redirect('/login/')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password =  request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
    data= {
        'form':LoginForm
    }
    return render(request,'login.html',context= data)


def register(request):
    if request.method=='POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('/login/')

        else:
            data = {
                'form': form
            }
            return render(request,'register.html',context=data)
    data={
        'form':RegisterForm()
    }
    return render(request,'register.html',context=data)


