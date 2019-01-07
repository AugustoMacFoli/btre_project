from django.shortcuts import render
from listings.models import Listing
from listings.filter_values import bedroom_choices, price_choices, state_choices
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp = Realtor.objects.filter(is_mvp=True)
    if mvp:
        mvp = mvp[0]
    context = {
        'realtors': realtors,
        'mvp': mvp
    }
    return render(request, 'pages/about.html', context)