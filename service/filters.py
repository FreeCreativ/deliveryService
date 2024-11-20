import django_filters
from .models import Order, Expense


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['status', 'rider', 'order_date', 'customer']


class ExpenseFilter(django_filters.FilterSet):
    class Meta:
        model = Expense
        fields = {
            'date': ['lt', 'gt'],  # Allows searching by partial name
            'category': ['exact'],  # Dropdown for exact match
            'status': ['exact'],  # Dropdown for exact match
            'payment_method': ['exact'],  # Dropdown for exact match
            'amount': ['lt', 'gt'],  # Less than and greater than filters
        }
