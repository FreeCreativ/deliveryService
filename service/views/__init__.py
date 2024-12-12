from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from service.models import Order, Expense
from .orders import OrderCreateView, OrderListView, OrderSuccessView, OrderDeleteView, OrderCancelUpdateView, \
    OrderCompleteUpdateView
from .customers import CustomerListView, CustomerDeleteView
from .expenses import ExpenseCreateView, ExpenseListView, ExpenseUpdateView, ExpenseDeleteView
from .review import ReviewListView


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'service/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_revenue = sum(order.amount for order in Order.objects.all())
        total_expenses = sum(expense.amount for expense in Expense.objects.all())
        context.update({
            'total_orders': Order.objects.count(),
            'pending_orders': Order.objects.filter(status='Pending').count(),
            'completed_orders': Order.objects.filter(status='Delivered').count(),
            'total_revenue': total_revenue,
            'total_expenses': total_expenses,
            'net_profit': total_revenue - total_expenses,
            'recent_orders': Order.objects.all()[:5],
            'recent_expenses': Expense.objects.all()[:5],
        })
        return context


class SupportVIew(TemplateView):
    template_name = 'service/support.html'
