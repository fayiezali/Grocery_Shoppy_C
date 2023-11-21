from django.urls import path
#
from . import views
#
#
#
urlpatterns = [
        path('password_change/', views.password_change_DEF, name="password_change-URL"),
]