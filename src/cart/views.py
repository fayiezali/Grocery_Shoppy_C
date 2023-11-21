from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from product. models      import *
from order_orderdetail. models import *
from tax. models      import *

#
#
#
# The Condition For Seeing The Required Page Login
@login_required(login_url="login/")
# View products in the cart
def cart_DEF(request):
    context = None # Set the value of the variable to nothing
    # trying to check if the user is authenticated and not anonymous.
    if request.user.is_authenticated \
        and not request.user.is_anonymous:
        # select all orders that the user is currently viewing and filter them to only show those that are not yet finished.
        if OrderMODEL.objects.all().filter(
            order_user= request.user ,
            order_is_finished=False):
            #  The code is trying to get the order that is finished.
            #  It does this by getting the OrderMODEL object and then checking if it has an attribute called "is_finished".
            #  If it doesn't have that attribute, then it will set its value to False.
            #  The code would result in an instance of the OrderMODEL class being retrieved for the user with id request.user .
            #  The order_is_finished attribute is set to False, meaning that this particular instance of the OrderMODEL class has not been finished yet.
            order_VAR = OrderMODEL.objects.get(
                order_user=request.user , 
                order_is_finished=False)
            OrderDetails_VAR = OrderDetailsMODEL.objects.all().filter(OrderDetails_order=order_VAR)
            total_VAR = 0
            # The iterative loop goes  all products
            for sub in OrderDetails_VAR:
                # Calculation multiply the price of the product by the quantity
                total_VAR += sub.OrderDetails_price * sub.OrderDetails_quantity
            #
            # tax_rate_VAR = Tax_MODEL.objects.all() 
            tax_rate_VAR = Tax_MODEL.objects.get()
            # 
            # ============================================================================
            # tax_rate_VAR = Tax_MODEL.objects.create(
            # tax_user=request.user , 
            # tax_order=order_VAR)
            # print('Was Added To Cart For Old Order.')

            # Save User Name & Order Number In Table:Tax_MODER
            Tax_MODEL.objects.update(
                                    tax_user  = request.user  , # User 
                                    tax_order = order_VAR   # Order No
                                    )     
            # ============================================================================

            # Send context To Cart.html Page
            context = {
                'order_VAR':order_VAR, # Get Da
                'OrderDetails_VAR':OrderDetails_VAR,
                'total_VAR':total_VAR,
                'tax_rate_VAR':tax_rate_VAR,

            }
    return render (request , 'cart/cart.html' ,  context) # Go To Cart Page
#
#
#
# The Condition For Seeing The Required Page Login
@login_required(login_url="login/")
# Add To Cart
def add_to_cart_DEF(request):
    # Validate the input
    # trying to check if the user is authenticated and not anonymous.
    if 'pro_id' in request.GET \
        and 'qty' in request.GET \
        and  request.user.is_authenticated \
        and not request.user.is_anonymous:
        # Save Data In Variables / Return the product that was requested by the user.
        pro_id_VAR = request.GET['pro_id'] # Save Product ID In Variables - pro_id:product ID - qty:Quantity
        qty_VAR    = request.GET['qty'] # Save Quantity In Variables
        # select all orders that the user is currently viewing and filter them to only show those that are not yet finished.
        order_VAR = OrderMODEL.objects.all().filter(
            order_user=request.user , 
            order_is_finished=False)
        # attempts to check if the product exists in the database.
        if not ProductMODEL.objects.all().filter(id=pro_id_VAR).exists():
            return redirect("dashboard-URL") # Go To Home/index Page
        # retrieves the product with id pro_id_VAR from the ProductMODEL.
        pro_VAR = ProductMODEL.objects.get(id=pro_id_VAR)
        
        if order_VAR:
            #  The code is trying to get the order that is finished.
            #  It does this by getting the OrderMODEL object and then checking if it has an attribute called "is_finished".
            #  If it doesn't have that attribute, then it will set its value to False.
            #  The code would result in an instance of the OrderMODEL class being retrieved for the user with id request.user .
            #  The order_is_finished attribute is set to False, meaning that this particular instance of the OrderMODEL class has not been finished yet.
            old_order_VAR = OrderMODEL.objects.get(
                order_user=request.user , 
                order_is_finished=False)
            # Verify that the product does not already exist
            if OrderDetailsMODEL.objects.all().filter(
                OrderDetails_order=old_order_VAR , 
                OrderDetails_product=pro_VAR).exists():
                orderdetails_VAR = OrderDetailsMODEL.objects.get( 
                    OrderDetails_order=old_order_VAR , 
                    OrderDetails_product=pro_VAR)
                # Increase the quantity of the product in the cart
                orderdetails_VAR.OrderDetails_quantity += int(qty_VAR)
                orderdetails_VAR.save()# save Product and New_quantity
                # Send Messages To User
                messages.success(request    , "Product Quantity Has Been Increased.")

            else:
                # The code creates a new order with the same product and quantity as an old order.
                # The price is set to the current price of the product, which was calculated in the previous line.
                # The code will create a new order in the system with the same details as the old order.
                orderdetails_VAR = OrderDetailsMODEL.objects.create(
                    OrderDetails_product=pro_VAR , 
                    OrderDetails_order = old_order_VAR , 
                    OrderDetails_price=pro_VAR.product_price ,
                    OrderDetails_quantity=qty_VAR)
                # Send Messages To User
                messages.success(request    , "Was Added To Cart For Old Order.")
        else:
        #  creates a new order with the same product and quantity as an old order.
        #  The price is set to the current price of the product, which was calculated in the previous line.
        #  The code will create a new order in the system with the same details as the old order.
            new_order_VAR = OrderMODEL()
            new_order_VAR.order_user = request.user
            new_order_VAR.order_order_date = timezone.now()
            new_order_VAR.order_is_finished = False
            new_order_VAR.save()
            #  The code creates an instance of the OrderDetails model.
            #  The code then assigns a product to the order, and sets the price for that product.
            #  Next, it creates an instance of the Quantity model and sets its value to qty_VAR.
            #  Finally, it saves this new object in the database using OrderDetailsMODEL.objects.create().
            #  The code first declares a variable called pro_VAR which is set equal to Product1 .
            #  Then it declares another variable called new_order_VAR which is set equal to NewOrder1 .
            #  It also declares a third variable called PriceProd1 , which is set equal to Product1 's price .
            #  Lastly, it declares a fourth variable called QtyProduct1 , which is set equal to 1 (meaning one).
            #  Next, we create an instance of our OrderDetails model by calling objects.create() on our class's Model class with three parameters: OrderDetails_product=pro_VAR , OrderDetails _order=new_order _ V AR , and PriceProd1 =pro _ V AR .price
            #  The code will create a new OrderDetails model instance with the product and order fields set to pro_VAR and new_order_VAR, respectively.
            #  The price field is set to pro_VAR.product_price, while the quantity field is set to qty_VAR.
            orderdetails = OrderDetailsMODEL.objects.create(
                OrderDetails_product=pro_VAR , 
                OrderDetails_order=new_order_VAR , 
                OrderDetails_price=pro_VAR.product_price ,
                OrderDetails_quantity=qty_VAR)
            # Send Message To User
            messages.success(request    , "Added in The Cart.")
        return redirect("dashboard-URL") # Go To Home/index Page

    else:
        return redirect("dashboard-URL")  # Go To Home/index Page
#
#
#
# The Condition For Seeing The Required Page Login
@login_required(login_url="login/")
# Remove the product from the cart
def remove_from_cart_DEF(request , orderdetails_id):
    # trying to check if the user is authenticated and not anonymous.
    if request.user.is_authenticated \
        and not request.user.is_anonymous\
        and orderdetails_id:
            # The ID number of the product to be deleted is obtained
            orderdetails_VAR = OrderDetailsMODEL.objects.get(id=orderdetails_id)
            if orderdetails_VAR.OrderDetails_order.order_user.id == request.user.id:
                orderdetails_VAR.delete() # Delete The Product
    # Send Message To User
    messages.success(request    , "Deleted Successfully.")
    return redirect("cart-URL") # Go To Cart Page
#
#
#
# The Condition For Seeing The Required Page Login
@login_required(login_url="login/")
# Increase the quantity of the product in the cart
# def add_quantity_DEF(request , orderdetails_id):
def increase_quantity_product_in_cart_DEF(request , orderdetails_id):
    # trying to check if the user is authenticated and not anonymous.
    if request.user.is_authenticated \
        and not request.user.is_anonymous\
        and orderdetails_id:
            # The ID number of the product to be deleted is obtained
            orderdetails_VAR = OrderDetailsMODEL.objects.get(id=orderdetails_id)
            if orderdetails_VAR.OrderDetails_order.order_user.id == request.user.id:
                orderdetails_VAR.OrderDetails_quantity += 1  # Increase the quantity of the product in the cart
                orderdetails_VAR.save() #s save The quantity
    return redirect("cart-URL") # Go To Cart Page
#
#
#
# The Condition For Seeing The Required Page Login
@login_required(login_url="login/")
# Reduce the quantity of the product in the cart
# def sub_qty_DEF(request , orderdetails_id):
def reduce_quantity_product_in_cart_DEF(request , orderdetails_id):
    # trying to check if the user is authenticated and not anonymous.
    if request.user.is_authenticated \
        and not request.user.is_anonymous\
        and orderdetails_id:
            # The ID number of the product to be deleted is obtained
            orderdetails_VAR = OrderDetailsMODEL.objects.get(id=orderdetails_id)
            if orderdetails_VAR.OrderDetails_order.order_user.id == request.user.id:
                if orderdetails_VAR.OrderDetails_quantity > 1:  # Check whether the product quantity is greater than 1
                    orderdetails_VAR.OrderDetails_quantity -= 1  # Reduce the quantity of the product in the cart
                    orderdetails_VAR.save() #s save The quantity
    return redirect("cart-URL") # Go To Cart Page
#
#
#
