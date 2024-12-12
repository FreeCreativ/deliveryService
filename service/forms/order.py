from django import forms

from service.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_type', 'from_location', 'to_location', 'description', 'amount', 'to_location', 'customer']
