from django import forms

CATEGORY_CHOICES = [
    ('Fuel', 'Fuel'),
    ('Maintenance', 'Maintenance'),
    ('Packaging', 'Packaging'),
    ('Ticket', 'Ticket'),
    ('Rider', 'Rider Fee'),
    ('Others', 'Others'),
]


class ExpenseForm(forms.Form):
    exp_name = forms.CharField(label="Expense Name", max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'e.g. Buying of fuel'}))
    amount = forms.DecimalField(label="Amount", max_digits=10, decimal_places=2, required=True,
                                widget=forms.NumberInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Enter Expense Amount'}))
    category = forms.ChoiceField(label="Expense Category", choices=CATEGORY_CHOICES, required=True,
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    vendor = forms.CharField(label="Vendor", max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter vendor name'}))
