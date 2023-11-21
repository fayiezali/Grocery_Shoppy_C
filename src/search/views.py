from django.shortcuts import render, redirect
from order_orderdetail.models import *
from django.contrib.auth.models import User
#
#
#
def search_product_DEF(request):

    # Validate the input
    # trying to check if the user is authenticated and not anonymous.
    if request.method == "POST" and 'search' in request.POST:
        search_VAR = request.POST['search']
        products_search_VAR = ProductMODEL.objects.filter(product_name__contains=search_VAR)
        return render(request, "search/search.html", {'products_search_VAR':products_search_VAR})
    else:
        return render(request, "search/search.html")


