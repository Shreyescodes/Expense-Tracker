from django.urls import path
from home import api_views

urlpatterns = [
    path('addmoney/', api_views.AddmoneyInfoList.as_view(), name='addmoney-list'),
    # Add more API endpoints as needed
]
