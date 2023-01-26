from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51M9YFHJlmZdRcXoBZU5teG3m475ojbcUIoTPTDBvefiXgsR0ICuNe7OFx8x3TFOpnjXS1kMQER5BKtkCRVIGQAcV00yzX7y0Vf',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
