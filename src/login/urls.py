from django.urls import path
from . import views # This Views I Created It
#
#
# # AUTHENTICATION:-------------------------------------------------------------------------------------------------------
urlpatterns = [
        # Display Login Web Page
        path("login/"     , views.Login_DEF            , name="login-URL"), 
] 