from django import forms

from .models import Staff, BusinessSetting


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude = ('profile_image', 'staff_id')


class BusinessSettingsForm(forms.ModelForm):
    class Meta:
        model = BusinessSetting
        fields = '__all__'
