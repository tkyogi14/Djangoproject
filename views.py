from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'imageapp\home.html')

# from imageapp.forms import UserImageForm    
# from .models import UploadImage  


# def image(request):  
#     if request.method == 'POST':  
#         form = UserImageForm(request.POST, request.FILES)  
#         if form.is_valid():  
#             form.save()  
#             img_object = form.instance                
#             return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})  
#     else:  
#         form = UserImageForm()  
  
#     return render(request, 'imageapp\imageupload.html', {'form': form}) 
#
# for uploading images. 

from django.shortcuts import render
from .forms import ImageForm
from .models import Image


def image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'imageapp\image.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'imageapp\image.html', {'form': form})

def images(request):
    all_images=Image.objects.all()
    context={'all_images':all_images}
    return render(request, 'imageapp\images.html', context)


from .forms import ProductForm, OrderForm
from .models import Product


def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'imageapp\product.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ProductForm()
    return render(request, 'imageapp\product.html', {'form': form})

def products(request):
    all_products=Product.objects.all()
    context={'all_products':all_products}
    return render(request, 'imageapp\products.html', context)

def order(request, id):
    obj = get_object_or_404(Product, id =id)
    form = OrderForm(request.POST or None, instance = obj)
    data = Product.objects.get(id = id)
    if form.is_valid():
        form.save()
        return redirect('products')
    context = {'form':form, 'data':data}
    return render(request, 'imageapp/order.html', context)

def kart(request):
    Ordered_items = Product.objects.filter(order_status = True)
    print("Ordered Items :", Ordered_items)
    price = Product.objects.values('price')[0]
    total = 0
    total_value = 0
    for price in Ordered_items:
        print(price.price)
        print(price.items)
        total = price.price*price.items
        total_value = total_value+total
        print(total)

    print(total_value)
    context = {'Ordered_items':Ordered_items, 'total':total_value}
    return render(request, 'imageapp/kart.html', context)