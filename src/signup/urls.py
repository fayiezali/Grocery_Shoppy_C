from django.urls import path
from . import views # This Views I Created It
#
#
# # AUTHENTICATION:-------------------------------------------------------------------------------------------------------
urlpatterns = [
        # Display Login Web Page
        path("signup/"     , views.Signup_DEF            , name="signup-URL"),
        # Activate  User Account
        path('activate/<uidb64>/<token>', views.activate, name='activate'),
] 