from business.models import Staff
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView
from django_filters.views import FilterView

from service.filters import OrderFilter
from service.forms import OrderForm, CustomerForm
from service.models import Order, Customer


class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'service/order/add_order.html'
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('service:order_success')  # Redirect after order is added

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include Customer form in the context
        context['customer_form'] = CustomerForm()
        return context

    def post(self, request, *args, **kwargs):
        # Instantiate the order form and customer form with POST data
        order_form = OrderForm(request.POST)
        customer_form = CustomerForm()

        if order_form.is_valid():

            # Get the phone number from the customer form
            phone_number = request.POST['contact']
            # phone_number = customer_form.cleaned_data.get('contact')

            # Check if customer with this phone number already exists
            existing_customer = Customer.objects.filter(contact=phone_number).first()

            if existing_customer:
                # If the customer exists, associate this order with the existing customer
                order = order_form.save(commit=False)  # Save order without committing yet
                order.customer = existing_customer  # Associate order with the existing customer
                order.save()  # Save the order
                return redirect(self.success_url)  # Redirect to success page

            else:
                # If no customer exists, save the new customer and the order
                customer_form = CustomerForm(request.POST)
                if customer_form.is_valid():
                    customer = customer_form.save()  # Save the new customer
                    order = order_form.save(commit=False)
                    order.customer = customer  # Associate the order with the new customer
                    order.save()  # Save the order
                    return redirect(self.success_url)  # Redirect to success page

        # If forms are not valid, render the page with errors
        return render(request, self.template_name, {
            'order_form': order_form,
            'customer_form': customer_form
        })


class OrderSuccessView(TemplateView):
    template_name = 'service/order/order_success.html'


class OrderListView(LoginRequiredMixin, FilterView):
    model = Order
    template_name = 'service/order/orders_list.html'
    context_object_name = 'orders'
    filterset_class = OrderFilter
    riders = Staff.objects.filter(role='Rider')
    extra_context = {'riders': riders}


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'service/order/orders_delete.html'
    success_url = reverse_lazy('service:order_list')
    slug_url_kwarg = 'order_id'
    slug_field = 'order_id'


class OrderCompleteUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'service/order/orders_update.html'
    context_object_name = 'order'
    success_url = reverse_lazy('service:order_list')
    slug_url_kwarg = 'order_id'
    slug_field = 'order_id'
    fields = ['status', 'rider']


class OrderCancelUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'service/order/orders_update.html'
    context_object_name = 'order'
    success_url = reverse_lazy('service:order_list')
    slug_url_kwarg = 'order_id'
    slug_field = 'order_id'
    fields = ['status', 'cancel_reason']
