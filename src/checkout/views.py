from django.shortcuts import render
from django.contrib import messages
from .models import *
from order_orderdetail.models import *
from track_shipment.models import *
#
#
#
def checkout_DEF(request):
    context = None # Set the value of the variable to nothing
    # trying to check if the user is authenticated and not anonymous.
    # if request.user.is_authenticated \
        # and not request.user.is_anonymous:
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
            # Send context To Cart.html Page
            context = {
                'order_VAR':order_VAR,
                'OrderDetails_VAR':OrderDetails_VAR,
                'total_VAR':total_VAR,
            }
            return render(request, "checkout/checkout.html", context)




def checkout_confirm_DEF(request):
    context   = None # Set the value of the variable to nothing
    total_VAR = None     # Clear the variable data
    address_VAR= request.POST.get('address')
    city_VAR= request.POST.get('city')
    state_VAR= request.POST.get('state')
    zipcode_VAR= request.POST.get('zipcode')
    phone_number_VAR= request.POST.get('phone_number')
    payment_VAR= request.POST.get('payment')

    # select all orders that the user is currently viewing and filter them to only show those that are not yet finished.
    if OrderMODEL.objects.all().filter(order_user= request.user,order_is_finished=False):
            #  The code is trying to get the order that is finished.
            #  It does this by getting the OrderMODEL object and then checking if it has an attribute called "is_finished".
            #  If it doesn't have that attribute, then it will set its value to False.
            #  The code would result in an instance of the OrderMODEL class being retrieved for the user with id request.user .
            #  The order_is_finished attribute is set to False, meaning that this particular instance of the OrderMODEL class has not been finished yet.
        order_VAR = OrderMODEL.objects.get(order_user=request.user,order_is_finished=False)
        OrderDetails_VAR = OrderDetailsMODEL.objects.all().filter(OrderDetails_order=order_VAR)
        total_VAR = 0
            # The iterative loop goes  all products
        for sub in OrderDetails_VAR:
                # Calculation multiply the price of the product by the quantity
            total_VAR += sub.OrderDetails_price * sub.OrderDetails_quantity
                

                # Put the entered data into the fields
        shipping_adress = CheckoutDetail_MODEL.objects.create(
        address=address_VAR, city=city_VAR , 
        phone_number=phone_number_VAR , 
        state=state_VAR, zipcode=zipcode_VAR , 
        user=request.user , 
        total_amount=total_VAR , 
        order=order_VAR , 
        payment=payment_VAR)
        shipping_adress.save() # Save Data In Table

				#  The code is trying to get the order that is finished.
				#  It does this by getting the OrderMODEL object and then checking if it has an attribute called "is_finished".
				#  If it doesn't have that attribute, then it will set its value to False.
				#  The code would result in an instance of the OrderMODEL class being retrieved for the user with id request.user .
				#  The order_is_finished attribute is set to False, meaning that this particular instance of the OrderMODEL class has not been finished yet.
        order_finished_VAR = OrderMODEL.objects.get(order_user=request.user ,order_is_finished=False)

        order_finished_VAR.order_is_finished = True # user.OrderMODEL Filed Name (order_is_finished) = True

        order_finished_VAR.save() # Save Data in Table
# ============================================================================
        # Get Order ID From  Order Table
        # Greate Table ShipmentTrack
        # Save User Name & Order ID & Confirm'True' In  Table ShipmentTrack
        order_VAR = OrderMODEL.objects.filter(order_user=request.user,order_is_finished=True).first() # Get Order ID
        ShipmentTrackMODEL_VAR = ShipmentTrackMODEL() # Order tracking table
        ShipmentTrackMODEL_VAR.shipment_track_order_id = order_VAR.id # Order ID
        ShipmentTrackMODEL_VAR.shipment_track_confirmed_order = True
        ShipmentTrackMODEL_VAR.save() # Save Data
        # ============================================================================
        # Get All Products and Save In Variable
        products_all_VAR = ProductMODEL.objects.all()

        # Send context To Cart.html Page
        context = {
                    'order_VAR':order_VAR,
                    'OrderDetails_VAR':OrderDetails_VAR,
                    'total_VAR':total_VAR,
                    'products_all_VAR':products_all_VAR,
                }

    messages.success(request    , "Checkout successfully.")
    return render(request,'dashboard/index.html', context)













































# # VER:Variables        
def checkout_DEF_(request):
        # trying to check Request Method Is POST and if the user is authenticated and not anonymous
    if request.method == "POST" and request.user.is_authenticated and not request.user.is_anonymous:
        
        order_VAR_ = OrderMODEL.objects.get(
                order_user=request.user , 
                order_is_finished=False)
        OrderDetails_VAR_ = OrderDetailsMODEL.objects.all().filter(OrderDetails_order=order_VAR_)
        total_VAR_ = 0
            # The iterative loop goes  all products
        for sub in OrderDetails_VAR_:
                # Calculation multiply the price of the product by the quantity
            total_VAR_ += sub.OrderDetails_price * sub.OrderDetails_quantity
            # Send context To Cart.html Page
        #     context = {
        #         'order_VAR_':order_VAR_,
        #         'OrderDetails_VAR_':OrderDetails_VAR_,
        #         'total_VAR_':total_VAR_,
        # }

        # Verify the validity of the entered data
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        phone_number = request.POST['phone_number']
        payment = request.POST['payment']
        # Clear the variable data
        total_VAR = None 
        # select all orders that the user is currently viewing and filter them to only show those that are not yet finished.
        order_VAR = OrderMODEL.objects.get(order_user=request.user , order_is_finished=False)
            #  The code is trying to get the order that is finished.
            #  It does this by getting the OrderMODEL object and then checking if it has an attribute called "is_finished".
            #  If it doesn't have that attribute, then it will set its value to False.
            #  The code would result in an instance of the OrderMODEL class being retrieved for the user with id request.user .
            #  The order_is_finished attribute is set to False, meaning that this particular instance of the OrderMODEL class has not been finished yet.

        OrderDetails_VAR = OrderDetailsMODEL.objects.all().filter(OrderDetails_order=order_VAR)
        # The iterative loop goes  all products
        for sub in OrderDetails_VAR:
            total_VAR = 0
            # Calculation multiply the price of the product by the quantity
            total_VAR += sub.OrderDetails_price * sub.OrderDetails_quantity
            # Create a new record
            # Put the entered data into the fields
            shipping_adress = CheckoutDetail_MODEL.objects.create(
                address=address, city=city , 
                phone_number=phone_number , 
                state=state, zipcode=zipcode , 
                user=request.user , 
                total_amount=total_VAR , 
                order=order_VAR , 
                payment=payment)
            shipping_adress.save() # Save Data In Table
            #  The code is trying to get the order that is finished.
            #  It does this by getting the OrderMODEL object and then checking if it has an attribute called "is_finished".
            #  If it doesn't have that attribute, then it will set its value to False.
            #  The code would result in an instance of the OrderMODEL class being retrieved for the user with id request.user .
            #  The order_is_finished attribute is set to False, meaning that this particular instance of the OrderMODEL class has not been finished yet.
            order_finished_VAR = OrderMODEL.objects.get(order_user=request.user ,order_is_finished=False)

            order_finished_VAR.order_is_finished = True # user.OrderMODEL Filed Name (order_is_finished) = True

            order_finished_VAR.save() # Save Data in Table
            
            context = {
                    'order_VAR':order_VAR,
                    'OrderDetails_VAR':OrderDetails_VAR,
                    'total_VAR':total_VAR,
                    'order_VAR_':order_VAR_,
                    'OrderDetails_VAR_':OrderDetails_VAR_,
                    'total_VAR_':total_VAR_,
                    }
            messages.success(request, "Order Is Successfully.")
            return render(request, "checkout/checkout.html", context)
    return render(request, "checkout/checkout.html")


