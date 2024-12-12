from .staff import StaffDetailView, StaffDeleteView, StaffListView, StaffUpdateView, StaffCreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from ..forms import BusinessSettingsForm


class BusinessSettingView(LoginRequiredMixin, FormView):
    form_class = BusinessSettingsForm
    template_name = 'business/business_setting.html'
    success_url = reverse_lazy('service:dashboard')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RolePermissionsView(LoginRequiredMixin, TemplateView):
    template_name = 'business/role_permissions.html'


class UserManagementView(LoginRequiredMixin, TemplateView):
    template_name = 'business/user_management.html'


class SecuritySettings(LoginRequiredMixin, TemplateView):
    template_name = 'business/user_management.html'
