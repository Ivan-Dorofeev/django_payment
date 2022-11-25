import stripe
from django.conf import settings
from django.shortcuts import render

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


def main(request):
    all_products = Item.objects.all()
    context = {
        'all_products': all_products
    }
    return render(request, 'main.html', context)


def buy(request, id_product):
    prices = {
        10: 'price_1M7GRdEwLhYUZPgltXRLoAap',
        100: 'price_1M7GRuEwLhYUZPgljYZPT5GB',
        1000: 'price_1M5rhEEwLhYUZPgloadL3Ngm'
    }

    product = Item.objects.filter(id=id_product)
    if not product:
        return render(request, 'wrong_address.html')

    product_price = product[0].price
    product_name = product[0].name
    stripe_request = stripe.checkout.Session.create(
        success_url="http://localhost:8000/success.html",
        cancel_url="http://localhost:8000/cancel.html",
        mode="payment",
        line_items=[
            {
                "price": prices[product_price],
                "quantity": 1,
            },
        ],
    )
    session_id = stripe_request['id']
    payment_url = stripe_request['url']
    context = {'session_id': session_id,
               'payment_url': payment_url,
               'product_name': product_name
               }
    return render(request, 'buy.html', context)


def item_info(request, id_product):
    product = Item.objects.filter(id=id_product)
    if not product:
        return render(request, 'wrong_address.html')

    context = {'product': product[0]}
    return render(request, 'item_info.html', context)
