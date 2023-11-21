from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import *

# The Condition For Seeing The Required Page Login
# @login_required(login_url="login/")
# View the product_detail_DEF Page
def product_detail_DEF(request, product_id):
    products_details_VAR=ProductMODEL.objects.get(id=product_id)
    context={'products_details_VAR':products_details_VAR}
    return render(request,"product/product_detail.html",context)
