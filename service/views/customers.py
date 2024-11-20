from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DeleteView

from service.forms import CustomerForm
from service.models import Customer


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'service/customer_list.html'
    context_object_name = 'customers'


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'service/customer_delete.html'
    context_object_name = 'customer'
    slug_field = 'customer_id'
    slug_url_kwarg = 'customer_id'


class RegistrationView(FormView):
    form_class = CustomerForm
    template_name = 'service/registration_form.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
