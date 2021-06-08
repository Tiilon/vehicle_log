from django.urls import path
from .views import *

app_name = 'vehicle_api'

urlpatterns = [
    path('user/', add_user, name='user'),
    path('user-details/<id>/', user_update, name='user-details')
]