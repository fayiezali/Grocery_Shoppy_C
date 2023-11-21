from django.urls import path
from . import views

urlpatterns = [
    path("track_shipment/", views.track_shipment_DEF, name="track_shipment-URL"),
] 