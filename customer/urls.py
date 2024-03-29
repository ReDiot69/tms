from django.urls import path
from . import views

urlpatterns = [
    path('customer_store', views.customer_store, name="stores_data_to_db"),
    path('measurement', views.measurement, name="call_measurement_page"),
    path('accounts_detail', views.accounts_detail, name="display_accountDetail_from_db"),
    path('account', views.accounts, name="call_accounts_page"),
    path('customer', views.customer, name="call_customer_page"),
]
