from django.urls import path
from myproject.crm import views as c

app_name = 'crm'

urlpatterns = [
    path('customer/', c.CustomerList.as_view(), name='customer_list'),
    path('customer/add/', c.CustomerCreate.as_view(), name='customer_add'),
    path('customer/<int:pk>/', c.CustomerDetail.as_view(), name='customer_detail'),
    path(
        'customer/<int:pk>/edit/',
        c.CustomerUpdate.as_view(),
        name='customer_update'
    ),
    path(
        'customer/<int:pk>/delete/',
        c.customer_delete,
        name='customer_delete'
    ),
]
