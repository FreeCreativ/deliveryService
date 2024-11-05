from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from service.forms import ExpenseForm
from service.models import Expense


class ExpensesView(TemplateView):
    template_name = 'service/expenses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] = [
            # Your static expense data
        ]
        return context


class AddExpenseView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'service/add_expenses.html'
    success_url = reverse_lazy('dashboard')
