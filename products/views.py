from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
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

    
    context = {
        'products': products,
         # add the query to the context
         'search_term': query,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
