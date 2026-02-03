from django.urls import path
from .views import product_list
from .views import product_detail

urlpatterns = [
    path('', product_list, name='product_list'),
    path('detail/<int:id>/', product_detail, name='product_detail'),
    
]
