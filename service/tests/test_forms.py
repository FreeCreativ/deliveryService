from django.test import TestCase
from service.forms import OrderForm


class MyFormTestCase(TestCase):
    def test_valid_form(self):
        form_data = {'name': 'Test Name', 'value': 42}
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'name': '', 'value': 42}
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
