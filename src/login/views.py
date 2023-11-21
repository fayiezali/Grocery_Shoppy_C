from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate 

# Login To Applcation
def Login_DEF(request):
    # attempts to prevent the user from accessing a view that requires authentication.
    if request.user.is_authenticated:
        return redirect("/") # Go To Home/index Page
    else:
        # Verify the validity of the entered data
        if request.method == "POST" and  'button_login' in request.POST:
            username = request.POST['username'] # User Name 
            password = request.POST['password'] # Passwerd
            remember = request.POST.get('remember_me')
            user = authenticate(username=username, password=password)
            # Verify that the requested user exists
            if user is not None:
                # Check Selected/unselected Remember Me key
                if remember is None:
                    request.session.set_expiry(0)  # <-- Here if the remember me is False, that is why expiry is set to 0 seconds. So it will automatically close the session after the browser is closed.
                    messages.info(request    , "Session Expiry.")
                login(request, user) # Login To Applcation
                # Display a message to the user
                messages.success(request, f'Welcome: ( {username} )')
                # Go To Home Page
                return redirect("/")
            else:
                # Display a message to the user
                messages.error(request   , "User Name or Password Is Incorrect.") 
                # Display the login screen
                return render(request, "login/login.html")
    # Display the login screen
    return render(request, "login/login.html")
