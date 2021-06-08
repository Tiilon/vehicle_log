from django.urls import path
from django.views.generic import TemplateView

from .views import *

app_name = 'vehicle'

urlpatterns = [
    path('manager/', g_manager_view, name='general_manager_view'),
    path('branch/manager/<id>/', branch_manager_view, name='branch_manager'),
    path('branches/', branch_list, name='branches'),
    path('branch/details/<id>/', branch_details, name='branch_details'),
    path('car/details/<id>/', car_details, name='car_details'),
    path('assign/car/branch/<id>/', assign_car_branch, name='assign_car_branch'),
    path('respond/request/<id>/', respond_request, name="respond_request"),
    path('manager/requests/<id>/', manager_request, name='manager_requests'),
    path('manager/staff/list/', staff_list_gm, name='manager_staff_list'),
    path('remove/manager/<id>/', remove_manager, name='remove_manager'),
    path('bm/staff/list/<id>/', branch_staff_list, name='branch_staff_list'),
    path('all/requests/', all_req, name='all_requests'),
    path('admin-layout/', TemplateView.as_view(template_name='layout/admin_layout.html'))
]