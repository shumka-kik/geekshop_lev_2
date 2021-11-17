from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
import json

from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product


@login_required
def basket(request):
    popular_product = Product.objects.all().order_by('-price')[:4]
    data_category = ProductCategory.objects.all()
    count_basket_products = get_count_products_in_basket(request)
    basket_products = []
    basket_summ = 0

    if request.user.is_authenticated:
        basket_products = Basket.objects.filter(user=request.user).order_by('product__category')
        basket_summ = sum(bask.quantity * bask.product.price for bask in basket_products)

    with open('static/file_to_load_links.json') as file:
        data_links = json.load(file)

    content = {
        'title': 'Корзина',
        'popular_product': popular_product,
        'basket_products': basket_products,
        'categories': data_category,
        'count_basket_products': count_basket_products,
        'basket_summ': basket_summ,
        'links': data_links
    }
    return render(request, 'basketapp/shoppingcart.html', content)


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:productdetail', args=[pk]))

    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    basket = get_object_or_404(Basket, pk=pk)

    if basket:
        basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_products = Basket.objects.filter(user=request.user). \
            order_by('product__category')

        basket_summ = sum(bask.quantity * bask.product.price for bask in basket_products)

        content = {
            'basket_products': basket_products,
            'basket_summ': basket_summ,
        }

        result = render_to_string('basketapp/includes/inc_basket_list.html', \
                                  content)

        return JsonResponse({'result': result})


def get_count_products_in_basket(request):
    # Товары в корзине, отображаем количество в хэдере
    count_basket_products = 0

    if request.user.is_authenticated:
        count_basket_products = len(Basket.objects.filter(user=request.user))

    return count_basket_products
