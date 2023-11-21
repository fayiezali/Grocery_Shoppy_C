from django.urls import path
from . import views # This Views I Created It
#
#
# # AUTHENTICATION:-------------------------------------------------------------------------------------------------------
urlpatterns = [
        # Logout From Application
        path("logout/", views.Logout_DEF, name="logout-URL"),
] 