from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User # إستيراد اسم المستخدم
#for password hashing
from django.contrib.auth.hashers import make_password, check_password
#for Regex (regular expression)
#for email sending
# from django.conf import settings
# import random
# from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import send_mail

# VAR:variable
def password_change_DEF(request):
    # Check the Post's use that hides the entered data
    # if request.method == 'POST':
    if request.method == "POST" and  'password_change_button' in request.POST:
    # take all field entered by user so we cam work with them on backend
        password_old_VAR      = request.POST['curent_password']      # Curnet password
        password_new_VAR      = request.POST['new_password']        # New password    
        password_confirm_VAR  = request.POST['confirm_new_password'] # Confirm new password

        # New Password - Verify the authenticity of the entered data
        if password_new_VAR.isnumeric() and password_new_VAR.islower() and  password_new_VAR.isalnum() and  password_new_VAR.isalpha() and  password_new_VAR.isdigit() and  password_new_VAR.isupper():
            messages.error(request, "The Password must contain numeric & characters & lowercase & uppercase & symbol")
            return redirect('password_change-URL')

        # Ole Password - Verify the authenticity of the entered data
        if password_old_VAR == password_new_VAR:
            messages.error(request , 'You cannot set old password as new password...')
            return redirect('password_change-URL')

        # Old Password - Verify the authenticity of the entered data
        if len(password_old_VAR)>20:
            messages.error(request, "password_old must be under 20 charcters!!")
            return redirect('password_change-URL')

        # Old Password - Verify the authenticity of the entered data
        if len(password_old_VAR) ==0 or len(password_old_VAR) <=7 or len(password_old_VAR) =='':
            messages.error(request, "password_old -  The more than 8 characters, and must contain uppercase, number & symbol")
            return redirect('password_change-URL')

        # New Password - Verify the authenticity of the entered data
        if len(password_new_VAR) ==0 or len(password_new_VAR) <=7 or len(password_new_VAR) =='':
            messages.error(request, "password_new - The more than 8 characters, and must contain uppercase, number & symbol")
            return redirect('password_change-URL')

        # Confirm Password - Verify the authenticity of the entered data
        if len(password_confirm_VAR) ==0 or len(password_confirm_VAR) <=7 or len(password_confirm_VAR) =='':
            messages.error(request, "password_confirm - The more than 8 characters, and must contain uppercase, number & symbol")
            return redirect('password_change-URL')

        # Confirm Password - Verify the authenticity of the entered data
        if password_confirm_VAR != password_new_VAR:
            messages.success(request , 'Password & Confirm Password do not match!')
            return redirect('password_change-URL')
        #  The code will find the user with the ID of request.user.id and return them to you.
        # Save the current user in the variable
        current_user_VAR = User.objects.get(id=request.user.id)
        # The code will check if the current user's password is the same as the old one.
        if current_user_VAR.check_password(password_old_VAR):
            #  The code sets the password for current_user to new_password.
            current_user_VAR.set_password(password_new_VAR)
            current_user_VAR.save() # Save New Password
            messages.success(request,'Password Changed Successfully! Please LogIn.') # send Message to the user
            return render(request, 'dashboard/index.html',{}) # Returen The Required HTML Page
    else:
        # messages.success(request , 'No POST')    
        return render(request, 'password_change/password_change.html',{})




















































































# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import *
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
# from .models import *
# import json
# from django.contrib.auth.models import User
# # from . inherit import cartData

# def password_change_DEF(request):
#     if not request.user.is_authenticated:
#         return redirect('/login')
#     # data = cartData(request)
#     # items = data['items']
#     # order = data['order']
#     # cartItems = data['cartItems']
#     if request.method == "POST":
#         current_password = request.POST['current_password']
#         new_password = request.POST['new_password']
#         try:
#             u = User.objects.get(id=request.user.id)
#             if u.check_password(current_password):
#                 u.set_password(new_password)
#                 u.save()
#                 # alert = True
#                 #Display a message to the user
#                 messages.success(request,'Password Changed Successfully! Please LogIn.') # send Message to the user
#                 return render(request, "password_change/password_change.html")
#             else:
#                 currpasswrong = True
#                 messages.error(request, "Password incorrect") 
#                 return render(request, "password_change/password_change.html")
#         except:
#             pass
#     messages.error(request, "Do You Really Want To Change Your Password?") 
#     return render(request, "password_change/password_change.html")
