from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PdfView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 
from django.views.decorators.cache import cache_control
from django.contrib.staticfiles.views import serve

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/<int:product_slug>/',views.show_product, name='product_detail'),
    path('cart/', views.show_cart, name='show_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('download/', PdfView.as_view(), name='download'),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name="login"),
    path('product/', views.product, name="product"),
    path('home/', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('kfa/', views.kfa, name='kfa'), 
    # path('process-payment/', views.process_payment, name='process_payment'),
    # path('payment-done/', views.payment_done, name='payment_done'),
    # path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
   
