from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from service.filters import ExpenseFilter
from service.forms import ExpenseForm
from service.models import Expense


class ExpenseListView(LoginRequiredMixin, FilterView):
    template_name = 'service/expense/expense.html'
    model = Expense
    context_object_name = 'expenses'
    filterset_class = ExpenseFilter


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    success_url = reverse_lazy('service:expense-list')
    slug_field = 'expense_id'
    slug_url_kwarg = 'expense_id'
    template_name = 'service/expense/expense_update.html'
    fields = ['name', 'amount', 'category', 'vendor', 'status']


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    success_url = reverse_lazy('service:expense-list')
    slug_field = 'expense_id'
    slug_url_kwarg = 'expense_id'
    template_name = 'service/expense/expense_delete.html'


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'service/expense/add_expense.html'
    success_url = reverse_lazy('service:dashboard')
