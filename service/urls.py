from django.urls import path, include

from .views import (
    ReviewListView, OrderListView, ExpenseListView, CustomerListView, DashboardView,
    AddOrderView, ExpenseCreateView, OrderSuccessView, OrderDeleteView, CustomerDeleteView, SupportVIew,
    ExpenseDeleteView, ExpenseUpdateView
)

app_name = 'service'

customer_patterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('<str:customer_id>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
]
order_patterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('new/', AddOrderView.as_view(), name='add_order'),
    path('success/', OrderSuccessView.as_view(), name='order_success'),
    path('<orderId>/delete', OrderDeleteView.as_view(), name='order_delete'),
]
expense_patterns = [
    path('', ExpenseListView.as_view(), name='expense-list'),
    path('new/', ExpenseCreateView.as_view(), name='expense_add'),
    path('<str:expense_id>/update/', ExpenseUpdateView.as_view(), name='expense_update'),
    path('<str:expense_id>/delete/', ExpenseDeleteView.as_view(), name='expense_delete'),
]
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('orders/', include(order_patterns)),
    path('expenses/', include(expense_patterns)),
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('customers/', include(customer_patterns)),
    path('support/', SupportVIew.as_view(), name='support')
]
