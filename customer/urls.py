from django.conf.urls.static import static
from django.urls import path

from CreationDjango import settings
from . import views

urlpatterns = [
    path('customer_store', views.customer_store, name="stores_data_to_db"),
    path('measurement', views.measurement, name="call_measurement_page"),
    # path('accounts_detail', views.accounts_detail, name="display_accountDetail_from_db"),
    path('account', views.account, name="call_accounts_page"),
    path('historyacc', views.historyacc, name="call_history_accounts_page"),
    path('acceptorder', views.acceptorder, name="call_accept_order_page"),
    path('accepto', views.accepto, name="call_accept_order_page"),
    path('order', views.order, name="call_order_page"),
    path('billing', views.billing, name="call_billing_page"),
    path('dashboard', views.dashboard, name="call_dashboard_page"),
    path('search', views.orderSearch, name="searchBox"),
    path('change_emp', views.emp_change, name="searchBox"),
    path('next_payment', views.next_payment, name="searchBox"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
