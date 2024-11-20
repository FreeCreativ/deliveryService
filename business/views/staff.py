from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from business.models import Staff


class StaffCreateView(LoginRequiredMixin, CreateView):
    model = Staff
    template_name = 'business/staff/add_staff.html'  # Specify your template
    fields = [
        'role', 'name', 'phone_number', 'email', 'address',
        'state_of_origin', 'date_of_birth', 'emergency_contact',
        'start_date', 'position', 'pay_rate', 'bank_details',
        'vehicle_type', 'vehicle_reg_number', 'insurance_details',
        'driver_license', 'staff_agreement', 'verification_document'
    ]
    success_url = reverse_lazy('business:staff_list')  # Redirect to a staff list view after creation


class StaffListView(LoginRequiredMixin, ListView):
    model = Staff
    template_name = 'business/staff/staff.html'
    context_object_name = 'staff_list'


class StaffDetailView(LoginRequiredMixin, DetailView):
    model = Staff
    template_name = 'business/staff/profile.html'
    slug_url_kwarg = 'staff_id'
    slug_field = 'staff_id'
    context_object_name = 'staff'


class StaffDeleteView(LoginRequiredMixin, DeleteView):
    model = Staff
    template_name = 'business/staff/delete.html'
    slug_url_kwarg = 'staff_id'
    success_url = reverse_lazy('business:staff_list')
    slug_field = 'staff_id'


class StaffUpdateView(LoginRequiredMixin, UpdateView):
    model = Staff
    template_name = 'business/staff/Update.html'
    pk_url_kwarg = 'staff_id'
    success_url = reverse_lazy('business:staff_list')
    slug_field = 'staff_id'
