from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from product.models import *
from django.contrib.auth.models import User


# def categories_all_DEF(request):
#     category_VAR = CategoryMODEL.objects.all()
#     sub_category_VAR = SubCategoryMODEL.objects.all()
#     context={'category_VAR':category_VAR , 'sub_category_VAR':sub_category_VAR}
#     print(category_VAR)

#     return render(request, "dashboard/index.html", context)

def category_DEF(request):
    products_VAR = None
    
    categories_VAR = CategoryMODEL.objects.all()
    categoryID = request.GET.get('category_item')
    # print('category_ID:',categoryID)
    # print('Category_Name:',categories_VAR)
    if categoryID:
        products_VAR = ProductMODEL.get_all_products_by_categoryid(categoryID)
        # print('Products_Name_By_Category_ID:',products_VAR)
    else:
        products_VAR = ProductMODEL.objects.all();
        # print('Products_All:',products_VAR)
        
    context={'categories_VAR':categories_VAR , 'products_all_VAR':products_VAR}
    
    return render(request, "dashboard/index.html", context)


def sub_category_DEF(request):
    products_VAR = None
    
    sub_categories_VAR = SubCategoryMODEL.objects.all()
    
    sub_category_id_VAR = request.GET.get('category_sub_item')
    # print('category_ID:',sub_category_id_VAR)
    # print('Category_Name:',sub_categories_VAR)

    if sub_category_id_VAR:
        print(sub_category_id_VAR)
        products_VAR = ProductMODEL.get_all_products_by_categoryid(sub_category_id_VAR)
        # print('Products_Name_By_Category_ID:',products_VAR)
    else:
        products_VAR = ProductMODEL.objects.all();
        # print('Products_All:',products_VAR)
        
    context={'sub_categories_VAR':sub_categories_VAR , 'products_all_VAR':products_VAR}
    
    return render(request, "dashboard/index.html", context)


# Filtering products based on category
def filtering_products_Based_on_category_DEF(request):
    products_VAR = None
    
    categories_VAR = CategoryMODEL.objects.all()
    # categories_VAR = SubCategoryMODEL.objects.filter(SubCat_slug='ELECTRONICS')

    
    # category_id_VAR = request.GET.get('category_menu_item')
    # print('category_ID:',category_id_VAR)
    print('filtering_products_Based_on_category_DEF:',categories_VAR)

    # if category_id_VAR:
    #     print(category_id_VAR)
    #     products_VAR = ProductMODEL.get_all_products_by_categoryid(category_id_VAR)
    #     print('Products_Name_By_Category_ID:',products_VAR)
    # else:
    #     products_VAR = ProductMODEL.objects.all();
    #     print('Products_All:',products_VAR)
        
    context={'categories_VAR':categories_VAR , 'products_all_VAR':products_VAR}
    
    return render(request, "dashboard/index.html", context)


def product_filter_menu_by_category_id_DEF(request , category_id):
    
    sub_categories_VAR = SubCategoryMODEL.objects.all()

    if category_id:
        products_all_VAR = ProductMODEL.objects.filter (product_category=category_id)
        
        context={'sub_categories_VAR':sub_categories_VAR ,'products_all_VAR':products_all_VAR }
        
        return render(request, 'dashboard/index.html' ,context) 
    else:
        products_all_VAR = ProductMODEL.objects.all()
        
        context={'sub_categories_VAR':sub_categories_VAR ,'products_all_VAR':products_all_VAR}
        
        return render(request,"dashboard/index.html",context)



# Fish				            6
# Frozen Food			        5
# Snack  Food			        5
# Canned, Dry & Packaged Food	5
# Beverages		                5
# Bedding	bedding			    4
# Bath				            4
# Furniture			            4
# Televisions			        1
# Laptops & Computers		    1
# Mobiles & Accessories		    1