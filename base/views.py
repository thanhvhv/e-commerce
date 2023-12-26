from django.shortcuts import render, redirect
from .models import Category, SubCategory, Product, CardItem, OderItem, Order, Color, Size
from .forms import ImageForm, ProductForm, ImageProduct, ColorForm, SizeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
def home(request):
    cates = Category.objects.all()
    new_items = Product.objects.filter(status='New')
    bestseller_items= Product.objects.filter(status='Best Seller')
    context = {"cates":cates, 'new_items':new_items, 'bestseller_items':bestseller_items}
    return render(request, "base/index.html", context)


@login_required(login_url='login')
def createProduct(request):
    productForm = ProductForm()
    imageForm = ImageForm()
    if request.method == 'POST':
        productForm = ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            newProduct = productForm.save()
            imageForm = ImageForm(request.POST, request.FILES)
            images = request.FILES.getlist('image')
            if imageForm.is_valid():
                for image in images:
                    ImageProduct.objects.create(image=image,product=newProduct)
            return redirect('home')
    context = {'imageForm':imageForm, 'productForm':productForm}
    return render(request, 'base/createProduct.html', context)


@login_required(login_url='login')
def create_color(request):
    form = ColorForm()
    colors = Color.objects.all()
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('create_color')
    context = {'form':form, 'colors':colors}
    return render(request, 'base/create_color.html', context)


@login_required(login_url='login')
def create_size(request):
    form = SizeForm()
    sizes = Size.objects.all()
    if request.method == 'POST':
        form = SizeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('create_size')
    context = {'sizes':sizes,'form':form}
    return render(request, 'base/create_size.html', context)
            


def detail(request, pk):
    cates = Category.objects.all()
    product = Product.objects.get(id=pk)
    item = CardItem()
    item.product = product
    item.user = request.user
    if request.method == 'POST':
        item.color = Color.objects.get(id=request.POST.get('color'))
        item.size = Size.objects.get(id=request.POST.get('size'))
        item.quantity = request.POST['quantity']
        item.save()
    context = {'product':product, 'cates':cates}
    return render(request, 'base/detail.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "User or Password wrong!!!")
    context = {}
    return render(request, 'base/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def cart(request):
    cates = Category.objects.all()
    items = CardItem.objects.all()
    listPrice = []
    listID = []
    listQuantity = []
    for x in items:
        listPrice.append(x.product.price)
        listID.append(x.id)
        listQuantity.append(x.quantity)
    context = {'cates':cates, 'items':items, 'listPrice':listPrice, 'listID':listID, 'listQuantity':listQuantity}
    return render(request, 'base/cart.html', context)


def checkout(request):
    cates = Category.objects.all()
    items = CardItem.objects.all()
    listPrice = []
    listID = []
    listQuantity = []
    if request.method == 'POST':
        for x in items:
            a = str(x.id)
            if request.POST.get(a):
                x.status = "Ordering"
                x.save()
    buy_items = CardItem.objects.filter(status='Ordering')
    for x in buy_items:
        listPrice.append(x.product.price)
        listID.append(x.id)
        listQuantity.append(x.quantity)
    context = {'cates':cates, 'buy_items':buy_items, 'listPrice':listPrice, 'listID':listID, 'listQuantity':listQuantity}
    return render(request, 'base/checkout.html', context)



def checkoutSuccess(request):
    cates = Category.objects.all()
    order = Order()
    if request.method == 'POST':
        order.user = request.user
        order.name = request.POST["name"]
        order.email = request.POST["email"]
        order.phone = request.POST["phone"]
        order.note = request.POST["note"]
        order.city = request.POST.get("city")
        order.district = request.POST.get("district")
        order.ward = request.POST.get("ward")
        order.street = request.POST["street"]
        order.payment = request.POST.get("payment")
        order.save()
    order1 = Order.objects.get(id=2)
    context = {'cates':cates, 'order':order1}
    return render(request, 'base/checkout_success.html', context)
    
        
def shop_category(request, pk_cate):
    check_search = 0
    cates = Category.objects.all()
    products = Product()
    if pk_cate == 'tat-ca-san-pham':
        products = Product.objects.all()
    else: 
        cate = Category.objects.get(id=pk_cate)
        
    if request.method == 'GET':
        temp = request.GET.get('search')
        if temp is not None:
            check_search = 1
            products = Product.objects.filter(
                name__icontains=temp
            )
    context = {'cates':cates, 'products':products, 'check_search':check_search}
    return render(request, 'base/shop.html', context)


def shop_subcategory(request, pk_cate, pk_subcate):
    cates = Category.objects.all()
    sub_cates = SubCategory.objects.filter(id=pk_subcate)
    context = {'cates':cates, 'sub_cates':sub_cates}
    return render(request, 'base/shop.html', context)


def test(request):
    cates = Category.objects.all()
    subs = SubCategory.objects.all()
    list_sub = []
    list_cate = []
    list_sub_parent = []
    for x in cates:
        list_cate.append(x.name)
    for x in subs:
        list_sub.append(x.name)
        list_sub_parent.append(x.parent_category.name)
    list_sub = json.dumps(list_sub)
    list_cate = json.dumps(list_cate)
    list_sub_parent = json.dumps(list_sub_parent)
    print(list_sub_parent)
    context = {'list_sub':list_sub, 'list_cate':list_cate, 'cates':cates, 'subs':subs, 'list_sub_parent':list_sub_parent}
    return render(request, 'base/test.html', context)
    
        
        
        
    
    
