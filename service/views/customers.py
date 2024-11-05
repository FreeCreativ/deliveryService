from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from service.forms import CustomerForm
from service.models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = 'service/customer_list.html'
    context_object_name = 'customers'


class RegistrationView(FormView):
    form_class = CustomerForm
    template_name = 'service/registration_form.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
