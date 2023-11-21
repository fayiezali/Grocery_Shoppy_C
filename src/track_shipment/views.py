from django.shortcuts import render, redirect
from .models import *
from order_orderdetail. models import *
from track_shipment. models import *
from django.contrib import messages
from django.contrib.auth.models import User
#
#
#
def track_shipment_DEF(request):
    # Verify the validity of the entered data
    if request.method == "POST":
        #  Receive user input
        order_id_VAR = request.POST['order_id']
        # Verify the number of input letters
        if len(order_id_VAR)<1: 
                # Display a message to the user
            messages.error(request, "Please enter the order/shipment number")
            # Go To Page track_shipment.html
            return redirect('track_shipment-URL')
        # Create a filter to get the order number
        shipment_track_VAR = ShipmentTrackMODEL.objects.filter(shipment_track_order_id=order_id_VAR)
        # Send variables/data to the requested page
        return render(request, "track_shipment/track_shipment.html", {'shipment_track_VAR':shipment_track_VAR })
    # Go To Page track_shipment.html
    return render(request, "track_shipment/track_shipment.html")
