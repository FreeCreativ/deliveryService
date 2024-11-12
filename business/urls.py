from django.urls import path
from .views import BusinessSettingView

app_name = 'business'

urlpatterns = [
    path('settings/', BusinessSettingView.as_view(), name='settings'),
]
