"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('', include('login.urls')),
    path('', include('logout.urls')),
    path('', include('signup.urls')), 
    path('', include('password_change.urls')), 
    path('', include('password_reset.urls')), 
    path('', include('product.urls')),  
    path('', include('cart.urls')),  
    path('', include('checkout.urls')),
    path('', include('search.urls')), 
    path('', include('track_shipment.urls')),  
    path('', include('category.urls')),  

 
    # path('', include('tax.urls')),  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 