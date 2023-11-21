from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
import re
#
from project import settings
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes 
from . tokens import generate_token
# from django.utils.encoding import force_text
import django
from django.utils.encoding import force_str 
django.utils.encoding.force_text = force_str
import re
#
from django.contrib.auth import login 
#
#
# validation formula
EMAIL_REGEX        = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
USERNAME_REGEX     = re.compile("[a-z0-9_]{3,15}")
FIRSTNAME_REGEX    = re.compile("[a-zA-Z]{2,20}")
LASTNAME_REGEX     = re.compile("[a-zA-Z]{2,20}")
PASSWARD_Criterian = {
                    "length_criteria":".{8,}",
                    "lowercase_criteria":"[a-z]+",
                    "uppercase_criteria":"[A-Z]+",
                    "number_criteria":"[0-9]+",
                    "symbol_criteria":"[^A-Za-z0-9]+",
                    }
#
#
# VER:Variables        
def Signup_DEF(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        # Verify the validity of the entered data
        # if request.method == "POST":
        if request.method == "POST" and  'button_signup' in request.POST:
            # USER Model Fields:--------------------------------------------
            user_name_VAR             = request.POST['user_name']
            user_password_VAR         = request.POST['user_password']
            user_confirm_password_VAR = request.POST['user_confirm_password']
            email_VAR                 = request.POST['email']
            first_name_VAR            = request.POST['first_name']
            last_name_VAR             = request.POST['last_name']
            # PROFILE Model Fields:-------------------------------------------
            father_name_VAR           = request.POST['father_name']
            grand_father_name_VAR     = request.POST['grand_father_name']
            mobile_number_VAR         = request.POST['mobile_number']
            # ---------------------------------------------------------------
            # defining some parameter for user to follow while making account
            # Verify the validity of the inputs - UserName
            if not USERNAME_REGEX.match(user_name_VAR):
                # Display a message to the user
                messages.error(request, "User Name - The Entered Data Is incorrect") 
                return redirect('signup-URL')

            # Verify that the name is not used by another user
            if User.objects.filter(username=user_name_VAR):
                # Display a message to the user
                messages.error(request, "Username already exist! Please try some other username.")
                return redirect('signup-URL')

            # Verify the number of input letters
            if len(user_name_VAR)>20:
                # Display a message to the user
                messages.error(request, "Username must be under 20 charcters!!")
                return redirect('signup-URL')

            # Verify the validity of the inputs - Email
            if not EMAIL_REGEX.match(email_VAR):
                # Display a message to the user
                messages.error(request, "EMAIL - The Entered Data Is incorrect")
                return redirect('signup-URL')

            # Verify that the Email is not used by another user
            if User.objects.filter(email=email_VAR).exists():
                # Display a message to the user
                messages.error(request, "Email Already Registered!!")
                return redirect('signup-URL')

            # Check the passwords match
            if user_password_VAR != user_confirm_password_VAR:
                # Display a message to the user
                messages.error(request, "Passwords didn't Matched!!")
                # Return Redirect To This Page
                return redirect('signup-URL')
            # ---------------------------------------------------------------
            user_VAR = User.objects.create_user(
                    username=user_name_VAR , 
                    password   = user_password_VAR , 
                    email      = email_VAR ,
                    first_name = first_name_VAR ,
                    last_name  = last_name_VAR ,
                    is_active  = False #account of user is not activated
                    )
            profile_VAR = UserProfile_MODEL.objects.create(
                    pro_User            = user_VAR ,
                    Pro_FatherName      = father_name_VAR ,
                    Pro_GrandFatherName = grand_father_name_VAR ,
                    Pro_MobileNnumber   = mobile_number_VAR
                    )
            user_VAR.save() # save Data In Table 01
            profile_VAR.save() # save Data In Table 02
            # Display a message to the user
            messages.success(request, f'Welcome: ( {user_name_VAR} ) - Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.')
            #
            #
            # Welcome Email
            subject = "Welcome To Ecommerce Login!!"
            message_welcom_VAR = "Hello " + user_VAR.first_name + "!! \n" + "Welcome to our Space!! \nThank you for visiting our website.\n We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n$p@r$h\nCEO of nothing"        
            # the email we will be using to send it to teh the new user
            from_email = settings.EMAIL_HOST_USER
            # the user email
            to_list = [user_VAR.email]
            # fail_silently is used for the purpose that if teh email is not send, teh app should not crash 
            send_mail(subject, message_welcom_VAR, from_email, to_list, fail_silently=True)
            #
            #
            # email for confiramtion of the account activation
            current_site = get_current_site(request)  # it will traget the diamin of teh current site
            email_subject = "Confirm your Email @ Authentication - Django Login!!"
            # the email_confirmation.html is the template to be used for every time confimation email is sent
            # ("email_confirmation.html", {dict})
            message_confirm_VAR = render_to_string('signup/email_confirmation.html',{
                'name': user_VAR.first_name,
                'domain': current_site.domain,
                # getting user id
                'uid': urlsafe_base64_encode(force_bytes(user_VAR.pk)),
                # generating token with help of tokens.py
                'token': generate_token.make_token(user_VAR)
            })
            # creating an email object
            email = EmailMessage(
            email_subject,
            message_confirm_VAR,
            # person sending the mail
            settings.EMAIL_HOST_USER,
            # person to whom the mail is to be send
            [user_VAR.email],
            )
            email.fail_silently = True
            email.send()

        # now redirecting them to signin page
            # Return Redirect To This Page
            return render(request, "login/login.html")
    # If the current condition is met: (request.method == "POST" and  'button_signup' in request.POST:)Return Redirect To This Page
    return render(request, "signup/signup.html")
#
#
#
# for activating the account
def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        # fetching 
        myuser_VAR = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser_VAR = None

    if myuser_VAR is not None and generate_token.check_token(myuser_VAR,token):
        myuser_VAR.is_active = True
        # user.profile.signup_confirmation = True
        myuser_VAR.save()
        login(request,myuser_VAR)
        # Display a message to the user
        messages.success(request, "Your Account has been activated!!")
        # Return Redirect To This Page
        return redirect('signup-URL')
    else:
        # Display a message to the user
        messages.error(request, "Your Account activation failed!!")
        # Return Redirect To This Page
        return redirect('signup-URL')