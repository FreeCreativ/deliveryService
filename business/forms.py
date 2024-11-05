from django import forms

from .models import Staff, BusinessSetting


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'


class BusinessSettingsForm(forms.ModelForm):
    class Meta:
        model = BusinessSetting
        fields = '__all__'
