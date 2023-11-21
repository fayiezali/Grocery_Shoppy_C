from django.shortcuts import render , redirect
from django.contrib.auth import logout
from django.contrib import messages

# Logout  From Application
def Logout_DEF(request):
    logout(request)
    # Send Message
    messages.info(request    , "Logged out successfully.")
    # Go To The Home Page
    return redirect('dashboard-URL')
