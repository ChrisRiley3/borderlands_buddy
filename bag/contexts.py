from django.shortcuts import get_object_or_404
from weapons.models import Weapon


def bag_contents(request):

    bag_items = []
    total = 0
    weapon_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        weapon = get_object_or_404(Weapon, pk=item_id)
        total += quantity * weapon.price
        weapon_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'weapon': weapon,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'weapon_count': weapon_count,
        'grand_total': grand_total,
    }

    return context
