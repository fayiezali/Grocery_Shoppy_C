from django.urls import path
from . import views

# We are adding a URL called /All products & product_detail
urlpatterns = [
    #
    path('product_details/<int:product_id>' , views.product_detail_DEF   ,name='product_detail-URL'),

]
