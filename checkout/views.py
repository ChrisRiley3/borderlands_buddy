from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your bag')
        return redirect(reverse('weapons'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H08XoBEKpBrk2JM15CPwFM2k6SyUGXdkTx6tNRGNLBCKV8j4x8MSraxSGx8cfXZQQa1KxdMcHyWBSd4f56RhUe700ufQc8SG5',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
