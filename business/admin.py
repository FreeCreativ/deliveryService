from django.contrib import admin

from .models import Staff, BusinessSetting, Activity


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'profile_image',
        'staff_id',
        'role',
        'name',
        'phone_number',
        'email',
        'address',
        'state_of_origin',
        'date_of_birth',
        'emergency_contact',
        'start_date',
        'position',
        'pay_rate',
        # 'bank_name',
        # 'account_number',
        # 'account_name',
        'vehicle_type',
        'vehicle_reg_number',
        'insurance_details',
        'driver_license',
        'staff_agreement',
        'verification_document',
    )
    list_filter = ('date_of_birth', 'start_date')
    search_fields = ('name',)


@admin.register(BusinessSetting)
class BusinessSettingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'business_name',
        'started_date',
        'logo',
        'currency',
        'currency_symbol_placement',
        'business_email',
        'business_phone',
        'business_country',
        'business_state',
        'business_address',
    )
    list_filter = ('started_date',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff', 'name', 'description')
    list_filter = ('staff',)
    search_fields = ('name',)
