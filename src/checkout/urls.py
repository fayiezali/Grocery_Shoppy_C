from django.urls import path
from . import views

urlpatterns = [
    # Go To Payment page
    path("checkout/"        , views.checkout_DEF         , name="checkout-URL"),
    # Confirm The Payment Process
    path("checkout_confirm" , views.checkout_confirm_DEF , name="checkout_confirm-URL"),
]  
