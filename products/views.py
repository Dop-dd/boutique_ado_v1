from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
    
        if 'category' in request.GET:
            # split it into a list at the commas
            categories = request.GET['category'].split(',')
            # filter to only products whose category names are on the list
            products = products.filter(category__name__in=categories)
            # filter all categories down to the ones whose name is in the list from the URL.
            category = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                message.error(request, 'You did not enter any search criteria !')
                return redirect( reverse('products'))

            """ variable equal to a Q object. Where the name contains the query.
            Or the description contains the query."""
            
            queries = Q(name__icontains=query) |  Q(description__icontains=query)
            #  pass them to the filter method in order to actually filter the products
            products = products.filter(queries)

    # return the current sorting methodology
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        # add the query to the context
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
