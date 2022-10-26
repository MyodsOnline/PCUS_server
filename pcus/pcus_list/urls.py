from django.urls import path, include

from .views import get_test_data

urlpatterns = [
    path('', get_test_data, name='test_data')
]
