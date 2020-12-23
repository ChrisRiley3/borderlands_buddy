from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from weapons.models import Weapon


def view_bag(request):
    """ A view to render the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified weapon to the shopping bag """

    weapon = get_object_or_404(Weapon, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request,
                         f'Updated {weapon.name} quantity to {bag[item_id]}')

    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {weapon.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified weapon to the specified amount"""

    weapon = get_object_or_404(Weapon, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request,
                         f'Updated {weapon.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {weapon.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """A view to remove the weapon from the shopping bag"""

    try:
        bag = request.session.get('bag', {})
        weapon = get_object_or_404(Weapon, pk=item_id)
        bag.pop(item_id)
        messages.success(request, f'Removed {weapon.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
