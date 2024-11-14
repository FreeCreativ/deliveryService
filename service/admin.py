from django.contrib import admin

from .models import Customer, Review, Expense, Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_id',
        'customer_name',
        'contact',
        'joined',
        'status',
    )
    list_filter = ('joined',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'review', 'date', 'date_modified')
    list_filter = ('date', 'date_modified')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'staff',
        'expense_id',
        'category',
        'name',
        'description',
        'amount',
        'vendor',
        'payment_method',
        'date',
        'status',
    )
    list_filter = ('staff', 'date')
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'rider',
        'customer',
        'order_id',
        'from_location',
        'to_location',
        'description',
        'amount',
        'order_type',
        'order_date',
        'status',
        'cancel_reason',
    )
    list_filter = ('rider', 'customer', 'order_date')