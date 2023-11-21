from django.db import models
from order_orderdetail.models import *
from django.contrib.auth.models import User # إستيراد اسم المستخدم

class CheckoutDetail_MODEL(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, db_constraint=False,null=True , blank=True)
    order = models.ForeignKey(OrderMODEL, on_delete=models.SET_NULL, db_constraint=False,null=True , blank=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    total_amount = models.CharField(max_length=10, blank=True,null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    payment = models.CharField(max_length=100, blank=True, null=True)
    date_added_auto= models.DateTimeField(auto_now_add=True)     

    # 'admin'display the field name on a page
    # \: write code of more than 1 line in the Python interpreter
    def __str__(self):
        return  'phone_number: ' + str(self.phone_number) + '-' \
                'User Name: ' + str(self.user) + '-' \
                'Order Id: ' + str(self.order.id) 
