from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from .forms import BusinessSettingsForm, StaffForm


class BusinessSettingView(LoginRequiredMixin, FormView):
    form_class = BusinessSettingsForm
    template_name = 'business/business_setting.html'
    success_url = reverse_lazy('service:dashboard')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreateStaffView(LoginRequiredMixin, CreateView):
    form_class = StaffForm
    template_name = 'business/add_staff.html'
    success_url = reverse_lazy('service:dashboard')
