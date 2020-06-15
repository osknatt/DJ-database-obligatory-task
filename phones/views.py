from django.shortcuts import render
from .models import Phone

def show_catalog(request):
    template = 'catalog.html'
    if 'sort' in request.GET:
        if request.GET['sort'] == 'name':
            all_phones = Phone.objects.all().order_by('name')
        elif request.GET['sort'] == 'min_price':
            all_phones = Phone.objects.all().order_by('price')
        elif request.GET['sort'] == 'max_price':
            all_phones = Phone.objects.all().order_by('-price')
    else:
        all_phones = Phone.objects.all()
    context = {
        'all_phones': all_phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
