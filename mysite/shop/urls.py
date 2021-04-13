from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about/', views.about, name='About'),
    path('tracker/', views.tracker, name='Tracker'),
    path('productview/<int:myid>', views.productview, name='ProductView'),
    path('search/', views.search, name='Search'),
    path('contact/', views.contact, name='Contact'),
    path('checkout/', views.checkout, name='Checkout'),
]
