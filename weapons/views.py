from django.shortcuts import render, get_object_or_404
from .models import Weapon


def all_weapons(request):
    """ A view to show all the weapons, including sorting and search queries  """

    weapons = Weapon.objects.all()

    context = {
        'weapons': weapons,
    }

    return render(request, 'weapons/weapons.html', context)


def weapon_detail(request, weapon_id):
    """ A view to show individual weapon details """

    weapon = get_object_or_404(Weapon, pk=weapon_id)

    context = {
        'weapon': weapon,
    }

    return render(request, 'weapons/weapon_detail.html', context)
