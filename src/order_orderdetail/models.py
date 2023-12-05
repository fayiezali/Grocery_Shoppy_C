from django.db import models
from .models import *
from product.models import *
from track_shipment.models import *
# from decimal import Decimal
from django.contrib.auth.models import User # إستيراد اسم المستخدم
#
#
class OrderMODEL(models.Model):
    order_user        = models.ForeignKey(User , on_delete = models.CASCADE)
    order_order_date  = models.DateTimeField(auto_now_add=True)
    order_details     = models.ManyToManyField(ProductMODEL , through='OrderDetailsMODEL')
    order_is_finished = models.BooleanField(default=False)
    class Meta:
        ordering = ('-order_order_date',)
        verbose_name = "Order"
        verbose_name_plural = "Orders" 
    #
    # 'admin'display the field name on a page
    # \: write code of more than 1 line in the Python interpreter
    def __str__(self):
        return  'User Name: ' + self.order_user.username + '-' \
                'Order Id: ' + str(self.id) 
    #
    def __str__(self):
        return   str(self.id) 
    #
    #
    # 
    #
    @property
    def get_order_number_PROPERTY(self):
        order_number_VAR=0
        order_number_VAR = self.orderdetailsmodel_set.all()
        for sub in order_number_VAR:
            # 
            return sub.OrderDetails_order.id
    #
    @property
    def get_count_of_items_PROPERTY(self):
        orderitems = self.orderdetailsmodel_set.all().count
        # total = sum([item.OrderDetails_product for item in orderitems])
        return orderitems
    # 
    @property
    def get_quantity_of_products_PROPERTY(self):
        orderitems = self.orderdetailsmodel_set.all()
        total = sum([item.OrderDetails_quantity for item in orderitems])
        return total
    #
    @property
    def get_subtotal_without_tax_PROPERTY(self):
        total_VAR=0
        orderitems = self.orderdetailsmodel_set.all()
        for sub in orderitems:
            # Calculation multiply the price of the product by the quantity
            total_VAR += sub.OrderDetails_price * sub.OrderDetails_quantity
        return total_VAR
#
# 
#
class OrderDetailsMODEL(models.Model):
    OrderDetails_product  = models.ForeignKey(ProductMODEL , on_delete = models.CASCADE)
    OrderDetails_order    = models.ForeignKey(OrderMODEL   , on_delete = models.CASCADE)
    # OrderDetails_price    = models.DecimalField(max_digits=10,decimal_places=2)
    OrderDetails_price    = models.IntegerField()
    OrderDetails_quantity = models.IntegerField()
    class Meta:
        ordering = ('-OrderDetails_order',)
        verbose_name = "Order Detail"
        verbose_name_plural = "Order Details" 

    # 'admin'display the field name on a page
    # \: write code of more than 1 line in the Python interpreter
    def __str__(self):
        return  'User Name : ' + str(self.OrderDetails_order.order_user) + ' - ' +\
                'Product: ' + self.OrderDetails_product.product_name + ' - ' +\
                'Order Id: ' + str(self.OrderDetails_order.id)
# ===============Example For - Property & Method============================
    # It performs the calculation - plural
    @property
    def get_sum_PROPERTY(self):
        total = 100 + 50
        return total 
    # You display all the required data
    @staticmethod
    def get_all_order_STATICMETHOD():
        send_result = OrderDetailsMODEL.objects.all()
        return send_result
    # It performs a logical process that contains conditions - if
    # Received Parmeter
    @staticmethod
    def is_adult_STATICMETHOD(age):
        if age > 18:
            send_result = 'Yes' 
            return send_result
        else:
            send_result = 'No' 
            return send_result
    # It performs a filter for the required data
    # Received Parmeter
    @staticmethod                                     # Model
    def get_orders_by_customer(customer_id):          # Model
        return OrderMODEL.objects.filter(order_user=customer_id).order_by('-order_order_date')
# ===============TESTING============================

    #
    @property
    def get_order_number_PROPERTY(self):

        order_number_VAR=0
        order_number_VAR = OrderDetailsMODEL.all()

        # order_number_VAR = self.orderdetailsmodel_set.all()
        for sub in order_number_VAR:
            # 
            return sub.OrderDetails_order.id

