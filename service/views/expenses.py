from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entry_form'] = ExpenseForm()  # Empty form for displaying
        return context

    def post(self, request, *args, **kwargs):
        # Handling update form submission
        if 'update_expense' in request.POST:
            expense_id = request.POST.get('expense_id')
            expense = get_object_or_404(Expense, id=expense_id)
            form = ExpenseForm(request.POST, instance=expense)
            if form.is_valid():
                form.save()
                return redirect('service:expense-list')
            # Handling delete form submission
        elif 'delete_expense' in request.POST:
            order_id = request.POST.get('entry_id')
            order = get_object_or_404(Expense, id=order_id)
            order.delete()
            return redirect('service:expense-list')

        return super().get(request, *args, **kwargs)


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
