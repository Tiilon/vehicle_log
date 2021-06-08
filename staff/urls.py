from django.urls import path
from staff.views import *

app_name = 'staff'

urlpatterns = [
    path('new/staff/', add_staff, name='new_staff'),
    path('staff/', staff_view, name='staff_view'),
    path('staff/update/<id>/', change_user_type, name='change-user-type'),
    path('make/request/', make_request, name='make_request'),
    path('staff/respond/request/<id>/', staff_respond_request, name='staff_respond_request'),
]