from django.urls import path
from . import views

urlpatterns = [
    # path("products_all", views.products_all_DEF, name="products_all-URL"),
    path('add_to_cart'                                                , views.add_to_cart_DEF                        , name='add_to_cart-URL'),
    # Show cart contents
    path('cart'                                                       , views.cart_DEF                               , name='cart-URL'),
    # Remove the product from the cart
    path('remove_from_cart/<int:orderdetails_id>'                      , views.remove_from_cart_DEF                    , name='remove_from_cart-URL'),
    # Increase the quantity of the product in the cart
    path('increase_quantity_product_in_cart/<int:orderdetails_id>'    , views.increase_quantity_product_in_cart_DEF   , name='increase_quantity_product_in_cart-URL'),
    # Reduce the quantity of the product in the cart
    path('reduce_quantity_product_in_cart/<int:orderdetails_id>'      , views.reduce_quantity_product_in_cart_DEF     , name='reduce_quantity_product_in_cart-URL'),
    #
    # path('product_details/<int:product_id>'                            , views.product_details_DEF                     , name='product_details-URL'), 

    # path("product_view/<int:myid>/", views.product_view, name="product_view"),

]  