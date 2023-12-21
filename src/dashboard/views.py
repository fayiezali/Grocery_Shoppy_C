from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from product.models import *
from order_orderdetail import *
from order_orderdetail.models import OrderMODEL , OrderDetailsMODEL 
# The Condition For Seeing The Required Page Login
# @login_required(login_url="login/")
# View the dashboard Page
from order_orderdetail import OrderDetailsMODEL
def dashboard_DEF(request):
# ===============TESTING============================
    #(1)Create an object from the model
    #(2) Call @propertt and Call @staticmethod
    OrderDetailsMODE_OBJECT = OrderDetailsMODEL()                                                   # 0
    OrderDetailsMODE_OBJECT.get_sum_PROPERTY                                                         # 1
    OrderDetailsMODE_OBJECT.get_all_order_STATICMETHOD()                                             # 2
    is_adult_STATICMETHOD_VAR = OrderDetailsMODE_OBJECT.is_adult_STATICMETHOD(20)                    # 3                              
    customer_id_VAR = request.user.id                                                                # 00
    get_orders_by_customer_VAR = OrderDetailsMODEL.get_orders_by_customer(customer_id_VAR)           # 4
    
    print('      get_example_PROPERTY-01: ' , OrderDetailsMODE_OBJECT.get_sum_PROPERTY)              # 1
    print('get_all_order_STATICMETHOD-02: ' , OrderDetailsMODE_OBJECT.get_all_order_STATICMETHOD())  # 2
    print('     is_adult_STATICMETHOD-03: ' , is_adult_STATICMETHOD_VAR)                             # 3
    print('               Custoner ID-00: ' ,customer_id_VAR)                                        # 00
    print('get_orders_by_customer_VAR-04: ' , get_orders_by_customer_VAR)                            # 4
# ===============TESTING============================
    get_order_user_PROPERTY_VAR = OrderDetailsMODE_OBJECT.get_order_user_PROPERTY(1)                    # 3                              
    print('get_order_user_PROPERTY_VAR-05: ' , get_order_user_PROPERTY_VAR)                            # 4

# ===============
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
    context={
                'products_all_VAR':products_all_VAR , 
                'sub_categories_VAR':sub_categories_VAR , 
                
                'OrderDetailsMODE_OBJECT'    : OrderDetailsMODE_OBJECT ,
                'is_adult_STATICMETHOD_VAR'  : is_adult_STATICMETHOD_VAR ,
                'customer_id_VAR'            : customer_id_VAR ,
                'get_orders_by_customer_VAR' : get_orders_by_customer_VAR ,
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

# =========
# def product_detail_DEF(request, product_id):
#     products_details_VAR=ProductMODEL.objects.get(id=product_id)
#     context={'products_details_VAR':products_details_VAR}
#     return render(request,"orders/product_details.html",context)



# ==========
#   # products                       = Products.get_all_products_by_categoryid(categoryID)
#     get_sum_PROPERTY_VAR       = OrderDetailsMODEL.get_sum_PROPERTY          # 
#     get_all_order_STATICMETHOD_VAR = OrderDetailsMODEL.get_all_order_STATICMETHOD()  # 
#     is_adult_STATICMETHOD_VAR      = OrderDetailsMODEL.is_adult_STATICMETHOD(20)     # 
#     data = {} 
#     data['get_sum_PROPERTY_data_VAR']       = get_sum_PROPERTY_VAR
#     data['get_all_order_STATICMETHOD_data_VAR'] = get_all_order_STATICMETHOD_VAR 
#     data['is_adult_STATICMETHOD_data_VAR']      = is_adult_STATICMETHOD_VAR 
#     #*****************************
#     categories = SubCategoryMODEL.get_all_categories()
#     products   = ProductMODEL.get_all_products()
#     data = {}
#     data['categories'] = categories
#     data['products']   = products
#     print('categories + products-data: ' , data)
#     #*****************************


