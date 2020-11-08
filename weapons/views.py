from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Weapon, Category, Review
from .forms import WeaponForm, ReviewForm


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
    reviews = Review.objects.filter(weapon=weapon_id)

    context = {
        'weapon': weapon,
        'reviews': reviews
    }

    return render(request, 'weapons/weapon_detail.html', context)


@login_required
def add_weapon(request):
    """ Add a weapon to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = WeaponForm(request.POST, request.FILES)
        if form.is_valid():
            weapon = form.save()
            messages.success(request, 'Successfully added weapon!')
            return redirect(reverse('weapon_detail', args=[weapon.id]))
        else:
            messages.error(request, 'Failed to add weapon. Please ensure the form is valid.')
    else:
        form = WeaponForm()
    template = 'weapons/add_weapon.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_weapon(request, weapon_id):
    """ Edit a weapon in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

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


@login_required
def delete_weapon(request, weapon_id):
    """ Delete a weapon from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    weapon = get_object_or_404(Weapon, pk=weapon_id)
    weapon.delete()
    messages.success(request, 'Weapon deleted!')
    return redirect(reverse('weapons'))


def add_review(request, weapon_id):
    """ A view for users to add a review """

    weapon = Weapon.objects.get(pk=weapon_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            reviews = form.save(commit=False)
            reviews.weapon = weapon
            reviews.save()
            messages.success(request, 'Successfully added a review!')
            return redirect(reverse('weapon_detail', args=[weapon.id]))
            reviews.objects.create(reviews=reviews)
        else:
            messages.error(request, 'Failed to add a review. Please ensure the form is valid.')
    else:
        form = ReviewForm()
    template = 'weapons/add_review.html'
    context = {
        'form': form,
        'weapon': weapon,
    }

    return render(request, template, context)
