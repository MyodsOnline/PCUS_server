from django.urls import path

from .views import get_all_zvk, get_gen_zvk, get_all_our, get_single_station


urlpatterns = [
    path('', get_all_zvk, name='all_zvk'),
    # path('viewed/', get_viewed_zvk, name='viewed_zvk'),
    path('gen/', get_gen_zvk, name='gen_zvk'),
    path('gen/test/', get_all_our, name='gen_test'),
    path('gen/test/<int:station_id>/', get_single_station, name='gen_detail'),
]
