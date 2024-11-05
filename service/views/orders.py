from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from service.forms import OrderForm
from service.models import Order


class AddOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'service/add_order.html'
    success_url = reverse_lazy('dashboard')

class OrderListView(ListView):
    model = Order
    template_name = 'service/orders.html'
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
