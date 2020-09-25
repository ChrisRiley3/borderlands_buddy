from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Weapon, Category
from .forms import WeaponForm


def all_weapons(request):
    """ A view to show all the weapons, including sorting and search queries  """

    weapons = Weapon.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    manufacture = None

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name, manufacture':
            sortkey = 'lower_name'
            weapons = weapons.annotate(lower_name=Lower('name'))
            manufacture = manufacture.annotate(lower_name=Lower('manufacture'))
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        weapons = weapons.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            weapons = weapons.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('weapons'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            weapons = weapons.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'weapons': weapons,
        'search_term': query,
        'current_category': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'weapons/weapons.html', context)


def weapon_detail(request, weapon_id):
    """ A view to show individual weapon details """

    weapon = get_object_or_404(Weapon, pk=weapon_id)

    context = {
        'weapon': weapon,
    }

    return render(request, 'weapons/weapon_detail.html', context)


def add_weapon(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = WeaponForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added weapon!')
            return redirect(reverse('add_weapon'))
        else:
            messages.error(request, 'Failed to add weapon. Please ensure the form is valid.')
    else:
        form = WeaponForm()
    template = 'weapons/add_weapon.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_weapon(request, weapon_id):
    """ Edit a weapon in the store """
    weapon = get_object_or_404(Weapon, pk=weapon_id)
    if request.method == 'POST':
        form = WeaponForm(request.POST, request.FILES, instance=weapon)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated weapon!')
            return redirect(reverse('weapon_detail', args=[weapon.id]))
        else:
            messages.error(request, 'Failed to update weapon. Please ensure the form is valid.')
    else:
        form = WeaponForm(instance=weapon)
        messages.info(request, f'You are editing {weapon.name}')

    template = 'weapons/edit_weapon.html'
    context = {
        'form': form,
        'weapon': weapon,
    }

    return render(request, template, context)
