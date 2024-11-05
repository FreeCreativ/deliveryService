from django.views.generic import TemplateView

from service.models import Order, Expense
from .orders import AddOrderView, OrderListView
from .customers import CustomerListView
from .expenses import AddExpenseView, ExpensesView
from .review import ReviewListView


class DashboardView(TemplateView):
    template_name = 'service/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'total_orders': Order.objects.count(),
            'pending_orders': Order.objects.filter(status='Pending').count(),
            'completed_orders': Order.objects.filter(status='Delivered').count(),
            'total_revenue': sum(order.amount for order in Order.objects.all()),
            'total_expenses': sum(expense.amount for expense in Expense.objects.all()),
            'net_profit': context['total_revenue'] - context['total_expenses'],
            'recent_orders': Order.objects.all()[:5],
            'recent_expenses': Expense.objects.all()[:5],
        })
        return context
