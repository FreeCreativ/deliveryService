from django.urls import path, include
from .views import BusinessSettingView, StaffDeleteView, StaffDetailView, StaffListView, StaffCreateView, \
    StaffUpdateView, RolePermissionsView

app_name = 'business'

staff = [
    path('', StaffListView.as_view(), name='staff_list'),
    path('new/', StaffCreateView.as_view(), name='staff_create'),
    path('<str:staff_id>/', StaffDetailView.as_view(), name='staff_detail'),
    path('<staff_id>/delete/', StaffDeleteView.as_view(), name='staff_delete'),
    path('<staff_id>/update/', StaffUpdateView.as_view(), name='staff_update'),
]
urlpatterns = [
    path('staff/', include(staff)),
    path('role-permission/', RolePermissionsView.as_view(), name='role_permission'),
    path('settings/', BusinessSettingView.as_view(), name='settings'),
]
