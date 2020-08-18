from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Weapon


def all_weapons(request):
    """ A view to show all the weapons, including sorting and search queries  """

    weapons = Weapon.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            weapons = weapons.filter(queries)

    context = {
        'weapons': weapons,
        'search_term': query,
    }

    return render(request, 'weapons/weapons.html', context)


def weapon_detail(request, weapon_id):
    """ A view to show individual weapon details """

    weapon = get_object_or_404(Weapon, pk=weapon_id)

    context = {
        'weapon': weapon,
    }

    return render(request, 'weapons/weapon_detail.html', context)
