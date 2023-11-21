from django.urls import path
from . import views # This Views I Created It
#
#
# # AUTHENTICATION:-------------------------------------------------------------------------------------------------------
urlpatterns = [
        # Display Login Web Page
        path("search_product/"                     , views.search_product_DEF     , name="search_product-URL"),
] 