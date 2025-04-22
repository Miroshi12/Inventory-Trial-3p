#from django.urls import path
#from . import views

#urlpatterns = [
  #  path('', views.index, name='index'),
  #  path('staff/', views.staff, name='staff')
#]

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='dashbd-index'),
    path('products/', views.products, name='dashbd-products'),
    path('products/delete/<int:pk>/', views.product_delete,
         name='dashbd-products-delete'),
    path('products/detail/<int:pk>/', views.product_detail,
         name='dashbd-products-detail'),
    path('products/edit/<int:pk>/', views.product_edit,
         name='dashbd-products-edit'),
    path('customers/', views.customers, name='dashbd-customers'),
    path('customers/detial/<int:pk>/', views.customer_detail,
         name='dashd-customer-detail'),
    path('order/', views.order, name='dashbd-order'),
]