from django.shortcuts import render
from .models import Weapon


def all_weapons(request):
    """ A view to show all the weapons, including sorting and search queries  """

    weapons = Weapon.objects.all()

    context = {
        'weapons': weapons,
    }

    return render(request, 'weapons/weapons.html', context)
