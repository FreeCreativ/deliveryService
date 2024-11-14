from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from service.forms import OrderForm, CustomerForm
from service.models import Order, Customer


class AddOrderView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'service/order/add_order.html'
    form_class = OrderForm
    success_url = reverse_lazy('service:order_success')  # Redirect after order is added

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_form'] = CustomerForm()  # Add the Customer form to the context
        return context

    def post(self, request, *args, **kwargs):
        # Instantiate the forms with POST data
        print(request.POST)
        order_form = OrderForm(request.POST)
        customer_form = CustomerForm(request.POST)

        # Check if the order form is valid
        if order_form.is_valid():
            customer = None  # Initialize the customer variable

            # If the customer form is valid, save the customer data
            if customer_form.is_valid():
                customer = customer_form.save()

            # If a new customer was created or a valid customer is selected, save the order
            if customer:
                order = order_form.save(commit=False)  # Don't commit yet to add the customer
                order.customer = customer  # Set the customer for the order
                order.save()  # Save the order

                return redirect('service:order_success')  # Redirect to dashboard or success page

            else:
                # If the customer form is invalid or no customer is selected, return the forms with errors
                return render(request, self.template_name, {'order_form': order_form, 'customer_form': customer_form})

        # If the order form is invalid, re-render the page with both forms and error messages
        return render(request, self.template_name, {'order_form': order_form, 'customer_form': customer_form})


class OrderSuccessView(TemplateView):
    template_name = 'service/order/order_success.html'


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'service/order/orders_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        status_filter = self.request.GET.get('status', 'all')
        if status_filter != 'all':
            return Order.objects.filter(status=status_filter)
        return Order.objects.all()

    def post(self, request, *args, **kwargs):
        order_id = request.POST.get('order_id')
        order = get_object_or_404(Order, id=order_id)

        if 'complete_order' in request.POST:
            order.status = 'completed'
        elif 'cancel_order' in request.POST:
            reason = request.POST.get('reason')
            order.status = 'cancelled'
            order.description += f"\nCancelled: {reason}"
        order.save()
        return redirect('order_list')
