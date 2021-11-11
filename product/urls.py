from . import views
from django.urls import path


urlpatterns = [
    path('' , views.products , name='products'),
    path('product' , views.product , name='product'),
    path('search' , views.search , name='search'),
    
]