from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from .forms import BusinessSettingsForm, StaffForm


class BusinessSettingView(FormView):
    form_class = BusinessSettingsForm
    template_name = 'service/business_settings.html'
    success_url = reverse_lazy('service:dashboard')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreateStaffView(CreateView):
    form_class = StaffForm
    template_name = 'business/add_staff.html'
    success_url = reverse_lazy('service:dashboard')
