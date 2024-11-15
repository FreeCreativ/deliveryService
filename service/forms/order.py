from django import forms

from service.models import Customer, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_type', 'from_location', 'to_location', 'description', 'amount', 'to_location', 'customer']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # Customize the customer field to display names
        self.fields['customer'].queryset = Customer.objects.all()
        self.fields['customer'].label = "Customer Name"
