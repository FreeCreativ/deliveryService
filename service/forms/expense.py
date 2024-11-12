from django import forms

from service.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
