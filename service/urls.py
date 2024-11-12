from django.urls import path

from .views import (
    ReviewListView, OrderListView, ExpensesView, CustomerListView, DashboardView,
    AddOrderView, AddExpenseView
)

app_name = 'service'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('add_order/', AddOrderView.as_view(), name='add_order'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('expenses/', ExpensesView.as_view(), name='expenses'),
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('add_expense/', AddExpenseView.as_view(), name='add_expense'),
]
