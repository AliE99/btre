from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing


# Create your views here.
def index(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing1 = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing1
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
    }
    return render(request, 'listings/search.html', context)
