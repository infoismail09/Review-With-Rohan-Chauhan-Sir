from django.contrib import admin
from django.urls import path, include
from Api.views import CustomizedDataView

urlpatterns = [
    path('customized-data/', CustomizedDataView.as_view(), name='customized-data'),
]