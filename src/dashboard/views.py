from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from product.models import *
from order_orderdetail import *
from order_orderdetail.models import OrderMODEL , OrderDetailsMODEL 
# The Condition For Seeing The Required Page Login
# @login_required(login_url="login/")
# View the dashboard Page
def dashboard_DEF(request):
# ===============TESTING============================
    get_total_VAR = OrderDetailsMODEL() 
    get_total_VAR.get_all_order_STATICMETHOD()
    print('get_total_VAR.get_example_PROPERTY: '       , get_total_VAR.get_example_PROPERTY)
    print('get_total_VAR.get_all_order_STATICMETHOD: ' , get_total_VAR.get_all_order_STATICMETHOD())
    print('get_total_VAR.is_adult_STATICMETHOD: '      , get_total_VAR.is_adult_STATICMETHOD(20))

# ===============TESTING============================
    products_VAR = None
    sub_categories_VAR = SubCategoryMODEL.objects.all()
    sub_category_id_VAR = request.GET.get('category_sub_item')
    if sub_category_id_VAR:
        print(sub_category_id_VAR)
        products_all_VAR = ProductMODEL.get_all_products_by_categoryid(sub_category_id_VAR)
        # print('Products_Name_By_Category_ID:',products_VAR)
    else:
        # Get All Products and Save In Variable
        products_all_VAR = ProductMODEL.objects.all();

    # Put the data to be displayed on the page in context
    context={'sub_categories_VAR':sub_categories_VAR , 
            'products_all_VAR':products_all_VAR , 
            'get_total_VAR':get_total_VAR ,
            }
    return render(request,'dashboard/index.html', context)
#
#
#
# # The Condition For Seeing The Required Page Login
# @login_required(login_url="login/")
# View the about Page
# @login_required(login_url='login/')
# def about(request):
#     context={}
#     return render(request,'dashboard/about.html',context)




# def product_detail_DEF(request, product_id):
#     products_details_VAR=ProductMODEL.objects.get(id=product_id)
#     context={'products_details_VAR':products_details_VAR}
#     return render(request,"orders/product_details.html",context)

