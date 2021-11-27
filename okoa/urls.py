from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url,include
from django.contrib.auth import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('paypal/',include('paypal.standard.ipn.urls')),
    # path('logout/', views.logout, {"next_page": '/'})
]
