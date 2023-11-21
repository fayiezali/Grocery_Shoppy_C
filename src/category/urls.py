from django.urls import path
#
from . import views
#
#
#
urlpatterns = [
        path('category_path'                                            , views.category_DEF                               , name='category-URL'),
        path('category_sub_path'                                        , views.sub_category_DEF                           , name='sub_category-URL'),
        path('category_menu_path'                                       , views.filtering_products_Based_on_category_DEF   , name='category_menu-URL'),
        path('category_menu_path'                                       , views.filtering_products_Based_on_category_DEF   , name='category_menu-URL'),
        # path('category_all_path/<int:category_id>'                    , views.filter_category_by_name_Fish_DEF           , name='filter_category_by_name_Fish-URL'),
        path('product_filter_menu_by_category_id/<int:category_id>'     , views.product_filter_menu_by_category_id_DEF     , name='product_filter_menu_by_category_id-URL'),

]


# Fish				        6
# Frozen Food			        5
# Snack  Food			        5
# Canned, Dry & Packaged Food	        5
# Beverages		                5
# Bedding	bedding		        4
# Bath				        4
# Furniture			        4
# Televisions			        1
# Laptops & Computers		        1
# Mobiles & Accessories		        1