from django.shortcuts import render
from django.template.defaultfilters import slugify  
from .models import Phone, Media, Review

# Create your views here.
def home(request):
    return render(request, 'index.html')

def create_product(request):
    images = request.POST.getlist('media')
    if request.method == 'POST':
        product = Phone.objects.create(
            brand = request.POST['brand'],
            model = request.POST['model'],    
            description = request.POST['description'], 
            price = request.POST['price'], 
            name = request.POST['name'], 
            storage = request.POST['storage'], 
            ram = request.POST['ram'], 
            battery_capacity = request.POST['battery_capacity'], 
            screen_size = request.POST['screen_size'], 
            os = request.POST['os'],
            color = request.POST['color'], 
            camera = request.POST['camera'],  
            slug = slugify(request.POST['name']),     
        )
        product.save()
        for image in images:
            media = Media.objects.create(
                phone = product,
                photo = image
            )
            media.save()
    return render(request, 'create-product.html')

def product(request):
    return render(request, 'single-product.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def category(request):
    return render(request, 'category.html')