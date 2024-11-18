from django.urls import path

from .views import (
    ReviewListView, OrderListView, ExpensesView, CustomerListView, DashboardView,
    AddOrderView, AddExpenseView, OrderSuccessView, OrderDeleteView
)

app_name = 'service'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('add_order/', AddOrderView.as_view(), name='add_order'),
    path('order_success/', OrderSuccessView.as_view(), name='order_success'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('<orderId>/delete', OrderDeleteView.as_view(), name='order_delete'),
    path('expenses/', ExpensesView.as_view(), name='expenses'),
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('add_expense/', AddExpenseView.as_view(), name='add_expense'),
]
